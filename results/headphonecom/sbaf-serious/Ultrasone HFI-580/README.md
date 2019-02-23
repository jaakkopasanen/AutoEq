# Ultrasone HFI-580
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -1.1; 28 -2.2; 31 -3.3; 34 -4.4; 37 -5.2; 41 -6.1; 45 -6.7; 49 -7.2; 54 -7.5; 60 -7.5; 66 -7.5; 72 -6.7; 79 -4.9; 87 -5.4; 96 -5.9; 106 -6.0; 116 -5.8; 128 -5.2; 141 -4.6; 155 -4.0; 170 -2.1; 187 -1.6; 206 -5.0; 227 -5.3; 249 -5.9; 274 -6.8; 302 -7.3; 332 -7.2; 365 -6.8; 402 -6.3; 442 -6.0; 486 -5.9; 535 -5.9; 588 -5.7; 647 -5.5; 712 -5.3; 783 -5.3; 861 -5.4; 947 -5.5; 1042 -5.5; 1146 -4.5; 1261 -5.4; 1387 -6.1; 1526 -6.9; 1678 -8.1; 1846 -9.4; 2031 -9.9; 2234 -9.8; 2457 -9.4; 2703 -9.9; 2973 -11.2; 3270 -12.9; 3597 -12.0; 3957 -10.6; 4353 -8.6; 4788 -6.0; 5267 -2.7; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -7.6; 8482 -10.8; 9330 -12.5; 10263 -11.1; 11289 -6.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 2.18 | 6.5 dB  |
| Peaking | 176 Hz  | 3.68 | 5.0 dB  |
| Peaking | 3451 Hz | 1.43 | -7.1 dB |
| Peaking | 5921 Hz | 2.09 | 8.9 dB  |
| Peaking | 9136 Hz | 2.75 | -7.5 dB |
| Peaking | 62 Hz   | 2.29 | -2.0 dB |
| Peaking | 81 Hz   | 3.84 | 2.0 dB  |
| Peaking | 310 Hz  | 3.82 | -1.5 dB |
| Peaking | 1172 Hz | 0.72 | 2.0 dB  |
| Peaking | 1918 Hz | 2.85 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.0 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB |
| Peaking | 125 Hz   | 1.41 | 2.6 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.7 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-580/Ultrasone%20HFI-580.png)