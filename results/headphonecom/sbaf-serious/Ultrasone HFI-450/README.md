# Ultrasone HFI-450
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -1.1; 60 -2.6; 66 -3.8; 72 -4.0; 79 -3.4; 87 -4.6; 96 -6.1; 106 -6.9; 116 -7.1; 128 -6.3; 141 -6.4; 155 -6.4; 170 -5.4; 187 -5.4; 206 -5.2; 227 -5.2; 249 -5.7; 274 -7.1; 302 -8.1; 332 -8.8; 365 -8.4; 402 -7.9; 442 -8.4; 486 -7.6; 535 -7.1; 588 -6.9; 647 -6.7; 712 -6.7; 783 -6.5; 861 -6.4; 947 -6.6; 1042 -6.4; 1146 -6.4; 1261 -6.5; 1387 -6.5; 1526 -6.3; 1678 -6.7; 1846 -8.7; 2031 -8.4; 2234 -7.5; 2457 -6.2; 2703 -4.4; 2973 -3.8; 3270 -4.3; 3597 -4.8; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -4.5; 5793 -2.7; 6373 -1.0; 7010 -4.8; 7711 -6.2; 8482 -6.9; 9330 -9.6; 10263 -8.8; 11289 -6.7; 12418 -7.6; 13660 -7.4; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ultrasone HFI-450 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ultrasone HFI-450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.78 | 6.9 dB  |
| Peaking | 2888 Hz | 4.03 | 4.0 dB  |
| Peaking | 4342 Hz | 2.33 | 10.4 dB |
| Peaking | 4880 Hz | 0.54 | -4.7 dB |
| Peaking | 6328 Hz | 3.9  | 7.4 dB  |
| Peaking | 111 Hz  | 4.26 | -1.8 dB |
| Peaking | 229 Hz  | 2.16 | 2.3 dB  |
| Peaking | 327 Hz  | 1.62 | -2.9 dB |
| Peaking | 1615 Hz | 1.45 | 1.7 dB  |
| Peaking | 1899 Hz | 3.97 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ultrasone%20HFI-450/Ultrasone%20HFI-450.png)