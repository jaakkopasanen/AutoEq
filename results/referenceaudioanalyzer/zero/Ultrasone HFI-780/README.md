# Ultrasone HFI-780
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.6; 28 -1.2; 31 -2.0; 34 -2.7; 37 -3.3; 41 -3.9; 45 -4.3; 49 -4.6; 54 -4.5; 60 -4.0; 66 -3.6; 72 -3.7; 79 -4.1; 87 -4.2; 96 -4.1; 106 -3.9; 116 -3.8; 128 -3.5; 141 -2.8; 155 -2.0; 170 -1.1; 187 -0.5; 206 -0.5; 227 -1.6; 249 -3.4; 274 -4.8; 302 -5.8; 332 -6.7; 365 -7.3; 402 -7.7; 442 -7.5; 486 -7.1; 535 -6.8; 588 -6.6; 647 -6.4; 712 -6.2; 783 -6.1; 861 -6.1; 947 -6.4; 1042 -6.4; 1146 -6.7; 1261 -7.0; 1387 -7.6; 1526 -8.5; 1678 -9.2; 1846 -9.6; 2031 -8.2; 2234 -5.1; 2457 -3.7; 2703 -5.7; 2973 -7.3; 3270 -8.2; 3597 -8.9; 3957 -9.4; 4353 -10.2; 4788 -11.0; 5267 -10.9; 5793 -9.0; 6373 -6.9; 7010 -7.6; 7711 -9.7; 8482 -10.3; 9330 -9.9; 10263 -10.9; 11289 -13.6; 12418 -15.4; 13660 -14.2; 15026 -9.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-780 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-780 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 187 Hz   | 2.01 | 6.1 dB  |
| Peaking | 1721 Hz  | 4.96 | -3.3 dB |
| Peaking | 4732 Hz  | 2.7  | -4.4 dB |
| Peaking | 12442 Hz | 1.6  | -9.3 dB |
| Peaking | 23 Hz    | 1.21 | 6.0 dB  |
| Peaking | 80 Hz    | 0.83 | 1.7 dB  |
| Peaking | 394 Hz   | 2.95 | -2.0 dB |
| Peaking | 2421 Hz  | 1.65 | -2.3 dB |
| Peaking | 2438 Hz  | 4.5  | 6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | 3.2 dB  |
| Peaking | 250 Hz   | 1.41 | 3.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -3.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20HFI-780/Ultrasone%20HFI-780.png)