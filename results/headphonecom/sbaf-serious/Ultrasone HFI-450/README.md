# Ultrasone HFI-450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.8; 54 -1.9; 60 -3.4; 66 -4.6; 72 -4.8; 79 -4.2; 87 -5.4; 96 -6.9; 106 -7.7; 116 -7.9; 128 -7.1; 141 -7.2; 155 -7.2; 170 -6.2; 187 -6.2; 206 -6.0; 227 -6.0; 249 -6.5; 274 -7.9; 302 -8.9; 332 -9.6; 365 -9.3; 402 -8.7; 442 -9.2; 486 -8.4; 535 -7.9; 588 -7.7; 647 -7.5; 712 -7.5; 783 -7.3; 861 -7.2; 947 -7.4; 1042 -7.2; 1146 -7.2; 1261 -7.3; 1387 -7.3; 1526 -7.1; 1678 -7.5; 1846 -9.5; 2031 -9.2; 2234 -8.3; 2457 -7.0; 2703 -5.2; 2973 -4.6; 3270 -5.1; 3597 -5.6; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -5.3; 5793 -3.6; 6373 -1.1; 7010 -5.3; 7711 -6.2; 8482 -7.5; 9330 -10.4; 10263 -9.6; 11289 -7.5; 12418 -8.4; 13660 -8.2; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.68 | 7.5 dB  |
| Peaking | 358 Hz  | 0.1  | -1.5 dB |
| Peaking | 4283 Hz | 2.98 | 7.1 dB  |
| Peaking | 6273 Hz | 7.61 | 5.5 dB  |
| Peaking | 9746 Hz | 3.15 | -4.2 dB |
| Peaking | 109 Hz  | 4.05 | -1.8 dB |
| Peaking | 227 Hz  | 1.8  | 2.5 dB  |
| Peaking | 324 Hz  | 2.02 | -2.7 dB |
| Peaking | 1867 Hz | 1.04 | 2.1 dB  |
| Peaking | 1955 Hz | 3.2  | -4.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.5 dB  |
| Peaking | 62 Hz    | 1.41 | 2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.5 dB |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)