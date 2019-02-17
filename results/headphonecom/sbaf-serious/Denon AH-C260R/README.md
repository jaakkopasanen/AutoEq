# Denon AH-C260R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.8; 25 -15.7; 28 -15.6; 31 -15.4; 34 -15.3; 37 -15.1; 41 -14.9; 45 -14.8; 49 -14.6; 54 -14.4; 60 -14.2; 66 -14.0; 72 -13.9; 79 -13.7; 87 -13.5; 96 -13.1; 106 -12.7; 116 -12.4; 128 -12.0; 141 -11.6; 155 -11.3; 170 -10.7; 187 -10.3; 206 -9.7; 227 -9.0; 249 -8.4; 274 -7.7; 302 -7.0; 332 -6.3; 365 -5.5; 402 -4.7; 442 -4.1; 486 -3.5; 535 -2.8; 588 -2.1; 647 -1.5; 712 -1.0; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -0.9; 1146 -1.1; 1261 -1.5; 1387 -2.1; 1526 -2.8; 1678 -3.3; 1846 -3.4; 2031 -3.5; 2234 -3.5; 2457 -3.6; 2703 -4.0; 2973 -4.4; 3270 -3.4; 3597 -1.9; 3957 -2.1; 4353 -3.9; 4788 -5.1; 5267 -5.9; 5793 -7.0; 6373 -5.7; 7010 -3.6; 7711 -2.3; 8482 -1.9; 9330 -3.6; 10263 -4.4; 11289 -0.8; 12418 -0.7; 13660 -0.7; 15026 -0.7; 16529 -0.9; 18182 -2.4; 20000 -0.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C260R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C260R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.19 | -14.8 dB |
| Peaking | 178 Hz   | 0.68 | -4.3 dB  |
| Peaking | 2410 Hz  | 1.48 | -3.1 dB  |
| Peaking | 5707 Hz  | 2.42 | -6.1 dB  |
| Peaking | 9943 Hz  | 6.07 | -3.8 dB  |
| Peaking | 839 Hz   | 2.25 | 1.5 dB   |
| Peaking | 1635 Hz  | 3.71 | -1.2 dB  |
| Peaking | 3009 Hz  | 2.25 | 1.9 dB   |
| Peaking | 3020 Hz  | 5.08 | -3.0 dB  |
| Peaking | 17829 Hz | 3.57 | -2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -15.8 dB |
| Peaking | 62 Hz    | 1.41 | -9.1 dB  |
| Peaking | 125 Hz   | 1.41 | -8.9 dB  |
| Peaking | 250 Hz   | 1.41 | -6.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C260R/Denon%20AH-C260R.png)