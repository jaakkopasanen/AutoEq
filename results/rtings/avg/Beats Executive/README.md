# Beats Executive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -2.0; 31 -4.0; 34 -5.7; 37 -7.1; 41 -8.8; 45 -10.1; 49 -11.3; 54 -12.6; 60 -13.8; 66 -14.9; 72 -15.7; 79 -16.6; 87 -17.5; 96 -18.3; 106 -19.0; 116 -19.6; 128 -20.1; 141 -20.4; 155 -20.5; 170 -20.5; 187 -20.2; 206 -19.7; 227 -18.9; 249 -17.8; 274 -16.3; 302 -14.5; 332 -12.5; 365 -10.3; 402 -8.6; 442 -7.9; 486 -8.3; 535 -8.0; 588 -7.7; 647 -7.7; 712 -7.6; 783 -7.0; 861 -5.7; 947 -6.1; 1042 -6.9; 1146 -8.1; 1261 -8.3; 1387 -10.0; 1526 -11.1; 1678 -11.8; 1846 -13.4; 2031 -14.4; 2234 -14.9; 2457 -15.1; 2703 -15.3; 2973 -16.4; 3270 -20.0; 3597 -17.0; 3957 -11.2; 4353 -12.3; 4788 -15.6; 5267 -12.9; 5793 -11.4; 6373 -12.0; 7010 -12.0; 7711 -14.9; 8482 -16.4; 9330 -16.0; 10263 -15.0; 11289 -13.2; 12418 -12.5; 13660 -15.2; 15026 -18.7; 16529 -17.8; 18182 -13.5; 20000 -13.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats Executive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Executive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 105 Hz   | 0.9  | -10.9 dB |
| Peaking | 204 Hz   | 1.33 | -9.9 dB  |
| Peaking | 2982 Hz  | 1.05 | -10.6 dB |
| Peaking | 8739 Hz  | 2.22 | -6.7 dB  |
| Peaking | 16138 Hz | 0.75 | -11.8 dB |
| Peaking | 23 Hz    | 1.37 | 7.4 dB   |
| Peaking | 54 Hz    | 1.79 | -2.6 dB  |
| Peaking | 949 Hz   | 1.52 | 2.6 dB   |
| Peaking | 1851 Hz  | 1.13 | -2.0 dB  |
| Peaking | 2680 Hz  | 5.8  | 2.9 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.4 dB   |
| Peaking | 62 Hz    | 1.41 | -6.9 dB  |
| Peaking | 125 Hz   | 1.41 | -12.4 dB |
| Peaking | 250 Hz   | 1.41 | -9.7 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB   |
| Peaking | 2000 Hz  | 1.41 | -7.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.7 dB  |
| Peaking | 16000 Hz | 1.41 | -15.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20Executive/Beats%20Executive.png)