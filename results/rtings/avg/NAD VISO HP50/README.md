# NAD VISO HP50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.8; 23 -1.8; 25 -1.9; 28 -2.0; 31 -2.0; 34 -2.0; 37 -2.0; 41 -1.8; 45 -1.6; 49 -1.5; 54 -1.5; 60 -1.7; 66 -2.1; 72 -2.6; 79 -3.0; 87 -3.5; 96 -4.0; 106 -4.5; 116 -5.0; 128 -5.6; 141 -5.9; 155 -6.2; 170 -6.5; 187 -6.7; 206 -6.7; 227 -6.6; 249 -6.6; 274 -6.6; 302 -6.4; 332 -5.9; 365 -5.4; 402 -4.9; 442 -4.4; 486 -4.7; 535 -5.1; 588 -5.1; 647 -5.1; 712 -4.6; 783 -3.9; 861 -3.5; 947 -3.2; 1042 -3.0; 1146 -2.8; 1261 -3.0; 1387 -3.5; 1526 -4.3; 1678 -5.2; 1846 -5.6; 2031 -5.4; 2234 -4.2; 2457 -2.5; 2703 -1.4; 2973 -0.7; 3270 -0.5; 3597 -0.6; 3957 -1.0; 4353 -1.9; 4788 -4.4; 5267 -5.2; 5793 -3.9; 6373 -2.8; 7010 -2.0; 7711 -3.8; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`NAD VISO HP50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NAD VISO HP50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.48 | 2.8 dB  |
| Peaking | 188 Hz  | 0.77 | -3.4 dB |
| Peaking | 1942 Hz | 4.53 | -2.6 dB |
| Peaking | 3212 Hz | 2.03 | 4.0 dB  |
| Peaking | 6890 Hz | 8.95 | 2.0 dB  |
| Peaking | 445 Hz  | 3.35 | 1.7 dB  |
| Peaking | 512 Hz  | 1.26 | -1.3 dB |
| Peaking | 1034 Hz | 2.18 | 1.6 dB  |
| Peaking | 4182 Hz | 5.67 | 1.3 dB  |
| Peaking | 5064 Hz | 5.96 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.6 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/NAD%20VISO%20HP50/NAD%20VISO%20HP50.png)