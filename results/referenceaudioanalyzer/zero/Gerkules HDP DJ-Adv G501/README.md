# Gerkules HDP DJ-Adv G501
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -8.4; 25 -9.1; 28 -10.1; 31 -10.6; 34 -11.0; 37 -11.1; 41 -11.3; 45 -11.4; 49 -11.4; 54 -11.3; 60 -11.0; 66 -10.8; 72 -10.5; 79 -10.5; 87 -10.5; 96 -10.5; 106 -10.3; 116 -10.0; 128 -9.9; 141 -9.8; 155 -9.6; 170 -9.2; 187 -8.8; 206 -8.6; 227 -8.5; 249 -8.2; 274 -7.9; 302 -7.6; 332 -7.2; 365 -6.7; 402 -6.2; 442 -5.7; 486 -5.4; 535 -5.3; 588 -5.5; 647 -6.1; 712 -7.0; 783 -7.8; 861 -8.3; 947 -8.2; 1042 -8.7; 1146 -9.7; 1261 -10.6; 1387 -10.9; 1526 -10.6; 1678 -9.9; 1846 -8.9; 2031 -7.3; 2234 -5.9; 2457 -4.8; 2703 -3.6; 2973 -2.6; 3270 -1.0; 3597 -0.5; 3957 -0.5; 4353 -2.0; 4788 -2.3; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.3; 8482 -8.6; 9330 -9.4; 10263 -8.2; 11289 -6.6; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Gerkules HDP DJ-Adv G501 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Gerkules HDP DJ-Adv G501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 59 Hz   | 0.41 | -4.8 dB |
| Peaking | 1447 Hz | 1.76 | -5.3 dB |
| Peaking | 3514 Hz | 1.58 | 6.0 dB  |
| Peaking | 5996 Hz | 2.54 | 5.5 dB  |
| Peaking | 8992 Hz | 2.65 | -4.1 dB |
| Peaking | 38 Hz   | 2.31 | -0.6 dB |
| Peaking | 72 Hz   | 2.16 | 0.8 dB  |
| Peaking | 337 Hz  | 0.47 | -0.9 dB |
| Peaking | 523 Hz  | 1.29 | 2.8 dB  |
| Peaking | 814 Hz  | 2.72 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.6 dB |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 8.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Gerkules%20HDP%20DJ-Adv%20G501/Gerkules%20HDP%20DJ-Adv%20G501.png)