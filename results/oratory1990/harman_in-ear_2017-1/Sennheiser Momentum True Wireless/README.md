# Sennheiser Momentum True Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.8; 25 -9.1; 28 -9.6; 31 -9.9; 34 -10.2; 37 -10.4; 41 -10.7; 45 -10.9; 49 -11.1; 54 -11.3; 60 -11.5; 66 -11.7; 72 -12.0; 79 -12.2; 87 -12.3; 96 -12.5; 106 -12.5; 116 -12.4; 128 -13.2; 141 -13.2; 155 -13.0; 170 -12.8; 187 -12.5; 206 -12.1; 227 -11.7; 249 -11.2; 274 -10.9; 302 -10.9; 332 -10.3; 365 -9.7; 402 -9.3; 442 -8.9; 486 -8.5; 535 -8.0; 588 -7.7; 647 -7.3; 712 -7.0; 783 -6.8; 861 -6.7; 947 -6.9; 1042 -7.3; 1146 -7.4; 1261 -7.2; 1387 -7.1; 1526 -6.7; 1678 -6.1; 1846 -5.3; 2031 -3.8; 2234 -1.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.0; 6373 -4.9; 7010 -7.7; 7711 -6.6; 8482 -7.9; 9330 -13.0; 10263 -14.8; 11289 -10.9; 12418 -10.6; 13660 -19.7; 15026 -29.8; 16529 -30.9; 18182 -22.6; 20000 -8.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser Momentum True Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum True Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.67 | -2.1 dB  |
| Peaking | 144 Hz   | 0.43 | -6.1 dB  |
| Peaking | 3895 Hz  | 0.91 | 7.8 dB   |
| Peaking | 15686 Hz | 1.33 | -22.7 dB |
| Peaking | 17611 Hz | 1.51 | -9.6 dB  |
| Peaking | 2352 Hz  | 0.97 | -4.3 dB  |
| Peaking | 2438 Hz  | 2.16 | 6.5 dB   |
| Peaking | 5536 Hz  | 5.93 | 3.2 dB   |
| Peaking | 9912 Hz  | 4.99 | -5.5 dB  |
| Peaking | 12122 Hz | 4.95 | 6.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -4.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 8.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -29.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sennheiser%20Momentum%20True%20Wireless/Sennheiser%20Momentum%20True%20Wireless.png)