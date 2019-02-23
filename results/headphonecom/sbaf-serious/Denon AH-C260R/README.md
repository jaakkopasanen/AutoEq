# Denon AH-C260R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.8; 23 -15.8; 25 -15.7; 28 -15.6; 31 -15.4; 34 -15.3; 37 -15.1; 41 -14.9; 45 -14.8; 49 -14.6; 54 -14.4; 60 -14.2; 66 -14.0; 72 -13.9; 79 -13.7; 87 -13.5; 96 -13.1; 106 -12.7; 116 -12.4; 128 -12.0; 141 -11.6; 155 -11.3; 170 -10.7; 187 -10.3; 206 -9.7; 227 -9.0; 249 -8.4; 274 -7.7; 302 -7.0; 332 -6.3; 365 -5.5; 402 -4.7; 442 -4.1; 486 -3.5; 535 -2.8; 588 -2.1; 647 -1.5; 712 -1.0; 783 -0.7; 861 -0.5; 947 -0.6; 1042 -0.9; 1146 -1.1; 1261 -1.5; 1387 -2.1; 1526 -2.8; 1678 -3.3; 1846 -3.4; 2031 -3.5; 2234 -3.5; 2457 -3.6; 2703 -4.0; 2973 -4.4; 3270 -3.4; 3597 -1.9; 3957 -2.1; 4353 -3.9; 4788 -5.1; 5267 -5.9; 5793 -7.0; 6373 -5.7; 7010 -3.6; 7711 -4.6; 8482 -4.9; 9330 -4.9; 10263 -4.9; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-C260R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C260R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.4dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 61 Hz   |  0.24 | -8.4 dB |
| Peaking | 788 Hz  |  0.7  | 5.2 dB  |
| Peaking | 3742 Hz |  5.03 | 3.1 dB  |
| Peaking | 5667 Hz |  5.65 | -2.5 dB |
| Peaking | 18 Hz   |  0.71 | -4.7 dB |
| Peaking | 22 Hz   |  0.5  | -0.4 dB |
| Peaking | 7063 Hz | 10.01 | 1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.6 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.1 dB   |
| Peaking | 1000 Hz  | 1.41 | 4.5 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C260R/Denon%20AH-C260R.png)