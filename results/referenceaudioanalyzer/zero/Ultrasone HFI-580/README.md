# Ultrasone HFI-580
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.9; 34 -1.8; 37 -2.9; 41 -4.0; 45 -4.9; 49 -5.6; 54 -6.1; 60 -6.3; 66 -6.1; 72 -5.8; 79 -5.7; 87 -5.7; 96 -5.4; 106 -4.9; 116 -4.4; 128 -3.7; 141 -2.8; 155 -1.7; 170 -0.9; 187 -0.5; 206 -0.7; 227 -1.3; 249 -2.1; 274 -3.3; 302 -4.5; 332 -5.3; 365 -5.9; 402 -6.5; 442 -6.9; 486 -6.8; 535 -6.4; 588 -6.1; 647 -5.8; 712 -5.6; 783 -5.4; 861 -5.4; 947 -5.6; 1042 -5.7; 1146 -5.4; 1261 -5.5; 1387 -6.0; 1526 -6.5; 1678 -6.9; 1846 -7.1; 2031 -7.1; 2234 -7.4; 2457 -8.2; 2703 -9.3; 2973 -10.5; 3270 -11.4; 3597 -11.1; 3957 -10.1; 4353 -8.5; 4788 -7.0; 5267 -6.1; 5793 -6.3; 6373 -5.9; 7010 -8.9; 7711 -13.9; 8482 -16.6; 9330 -15.8; 10263 -14.0; 11289 -13.9; 12418 -14.7; 13660 -12.9; 15026 -8.0; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 1.47 | 6.8 dB  |
| Peaking | 191 Hz   | 1.55 | 6.3 dB  |
| Peaking | 3300 Hz  | 2.96 | -5.2 dB |
| Peaking | 8702 Hz  | 3.43 | -9.5 dB |
| Peaking | 12344 Hz | 1.94 | -8.0 dB |
| Peaking | 442 Hz   | 3.25 | -1.4 dB |
| Peaking | 915 Hz   | 1.45 | 1.1 dB  |
| Peaking | 6078 Hz  | 4.76 | 2.7 dB  |
| Peaking | 16069 Hz | 4.52 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | 2.9 dB  |
| Peaking | 250 Hz   | 1.41 | 4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | -7.6 dB |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)