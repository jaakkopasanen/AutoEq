# Beats Powerbeats 2 Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.3; 23 -8.7; 25 -9.1; 28 -9.6; 31 -10.1; 34 -10.4; 37 -10.7; 41 -11.0; 45 -11.4; 49 -11.6; 54 -11.9; 60 -12.3; 66 -12.7; 72 -13.1; 79 -13.4; 87 -13.9; 96 -14.3; 106 -14.6; 116 -14.9; 128 -15.1; 141 -15.3; 155 -15.5; 170 -15.6; 187 -15.5; 206 -15.4; 227 -15.1; 249 -14.8; 274 -14.4; 302 -13.8; 332 -13.2; 365 -12.3; 402 -11.3; 442 -10.1; 486 -8.6; 535 -6.5; 588 -4.5; 647 -2.5; 712 -0.8; 783 -0.5; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.5; 1261 -0.6; 1387 -0.7; 1526 -0.9; 1678 -1.7; 1846 -3.5; 2031 -5.4; 2234 -5.9; 2457 -5.3; 2703 -3.1; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.9; 4788 -3.8; 5267 -5.7; 5793 -5.3; 6373 -5.2; 7010 -7.3; 7711 -8.4; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Powerbeats 2 Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Powerbeats 2 Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 78 Hz   | 0.36 | -4.9 dB |
| Peaking | 191 Hz  | 0.65 | -5.4 dB |
| Peaking | 398 Hz  | 0.98 | -5.3 dB |
| Peaking | 818 Hz  | 0.73 | 9.0 dB  |
| Peaking | 3694 Hz | 2.43 | 6.2 dB  |
| Peaking | 952 Hz  | 4.63 | -1.0 dB |
| Peaking | 1620 Hz | 2.14 | 2.6 dB  |
| Peaking | 2160 Hz | 2.3  | -3.6 dB |
| Peaking | 2936 Hz | 6.21 | 2.8 dB  |
| Peaking | 7522 Hz | 7.34 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -7.0 dB |
| Peaking | 250 Hz   | 1.41 | -8.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 8.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Powerbeats%202%20Wireless/Beats%20Powerbeats%202%20Wireless.png)