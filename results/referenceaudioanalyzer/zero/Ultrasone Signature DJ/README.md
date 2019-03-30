# Ultrasone Signature DJ
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -2.1; 25 -3.6; 28 -5.4; 31 -6.8; 34 -7.9; 37 -8.7; 41 -9.3; 45 -9.6; 49 -9.7; 54 -9.9; 60 -10.4; 66 -10.9; 72 -11.2; 79 -11.1; 87 -10.9; 96 -10.9; 106 -10.8; 116 -10.4; 128 -9.9; 141 -9.5; 155 -8.8; 170 -7.8; 187 -6.5; 206 -5.5; 227 -4.6; 249 -3.4; 274 -2.0; 302 -1.7; 332 -2.5; 365 -3.9; 402 -5.1; 442 -5.8; 486 -6.1; 535 -6.0; 588 -6.0; 647 -5.9; 712 -5.7; 783 -5.6; 861 -5.2; 947 -4.5; 1042 -4.1; 1146 -4.1; 1261 -4.2; 1387 -3.8; 1526 -3.3; 1678 -2.9; 1846 -2.5; 2031 -2.6; 2234 -3.2; 2457 -5.0; 2703 -7.6; 2973 -10.0; 3270 -11.6; 3597 -11.8; 3957 -10.6; 4353 -8.4; 4788 -6.8; 5267 -4.8; 5793 -1.9; 6373 -0.9; 7010 -5.7; 7711 -12.0; 8482 -15.5; 9330 -15.1; 10263 -12.6; 11289 -10.8; 12418 -10.1; 13660 -9.2; 15026 -7.0; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone Signature DJ GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone Signature DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 2.57 | 6.5 dB   |
| Peaking | 84 Hz   | 0.74 | -6.7 dB  |
| Peaking | 1040 Hz | 0.08 | 2.8 dB   |
| Peaking | 3463 Hz | 3.11 | -8.9 dB  |
| Peaking | 9315 Hz | 2.31 | -11.5 dB |
| Peaking | 293 Hz  | 1.69 | 7.3 dB   |
| Peaking | 372 Hz  | 0.65 | -4.5 dB  |
| Peaking | 1927 Hz | 2.08 | 2.9 dB   |
| Peaking | 6198 Hz | 4.25 | 8.3 dB   |
| Peaking | 7066 Hz | 0.34 | -1.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.5 dB |
| Peaking | 250 Hz   | 1.41 | 4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | -4.2 dB |
| Peaking | 16000 Hz | 1.41 | -1.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20Signature%20DJ/Ultrasone%20Signature%20DJ.png)