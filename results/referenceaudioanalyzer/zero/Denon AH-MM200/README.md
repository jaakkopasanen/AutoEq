# Denon AH-MM200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.9; 23 -15.8; 25 -15.8; 28 -15.8; 31 -15.9; 34 -16.0; 37 -16.1; 41 -16.2; 45 -16.1; 49 -16.0; 54 -15.9; 60 -15.8; 66 -15.9; 72 -15.8; 79 -15.6; 87 -15.5; 96 -15.2; 106 -15.1; 116 -14.8; 128 -14.5; 141 -13.9; 155 -13.1; 170 -12.0; 187 -10.8; 206 -9.2; 227 -7.4; 249 -6.5; 274 -6.6; 302 -6.8; 332 -6.7; 365 -6.5; 402 -6.4; 442 -6.5; 486 -6.7; 535 -7.0; 588 -7.4; 647 -7.7; 712 -7.9; 783 -8.2; 861 -8.4; 947 -8.6; 1042 -8.7; 1146 -8.7; 1261 -8.7; 1387 -8.4; 1526 -8.1; 1678 -7.6; 1846 -7.1; 2031 -6.5; 2234 -6.0; 2457 -5.6; 2703 -5.3; 2973 -4.8; 3270 -3.8; 3597 -2.7; 3957 -1.0; 4353 -0.5; 4788 -3.1; 5267 -5.3; 5793 -4.6; 6373 -3.6; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Denon AH-MM200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-MM200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 47 Hz   | 0.35 | -10.6 dB |
| Peaking | 1181 Hz | 1.58 | -2.5 dB  |
| Peaking | 2503 Hz | 2.22 | 0.3 dB   |
| Peaking | 4137 Hz | 2.14 | 5.8 dB   |
| Peaking | 18 Hz   | 1.37 | -2.9 dB  |
| Peaking | 52 Hz   | 0.75 | 1.9 dB   |
| Peaking | 164 Hz  | 0.72 | -4.6 dB  |
| Peaking | 243 Hz  | 1.18 | 5.6 dB   |
| Peaking | 6662 Hz | 8.36 | 2.5 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.8 dB |
| Peaking | 125 Hz   | 1.41 | -7.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Denon%20AH-MM200/Denon%20AH-MM200.png)