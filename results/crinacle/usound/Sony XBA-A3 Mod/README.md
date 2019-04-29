# Sony XBA-A3 Mod
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -2.8; 25 -3.1; 28 -3.5; 31 -3.8; 34 -4.0; 37 -4.2; 41 -4.4; 45 -4.7; 49 -4.9; 54 -5.2; 60 -5.5; 66 -5.8; 72 -6.1; 79 -6.4; 87 -6.8; 96 -7.2; 106 -7.5; 116 -7.7; 128 -7.9; 141 -8.0; 155 -8.0; 170 -7.9; 187 -7.7; 206 -7.6; 227 -7.3; 249 -7.0; 274 -6.6; 302 -6.2; 332 -5.8; 365 -5.7; 402 -6.0; 442 -5.7; 486 -5.3; 535 -5.2; 588 -5.1; 647 -4.7; 712 -4.1; 783 -3.7; 861 -3.6; 947 -3.7; 1042 -4.2; 1146 -5.1; 1261 -6.0; 1387 -6.7; 1526 -6.8; 1678 -6.2; 1846 -5.1; 2031 -3.7; 2234 -2.3; 2457 -1.1; 2703 -0.7; 2973 -0.8; 3270 -0.5; 3597 -0.7; 3957 -0.5; 4353 -3.4; 4788 -6.7; 5267 -3.4; 5793 -1.5; 6373 -4.6; 7010 -3.3; 7711 -4.5; 8482 -4.7; 9330 -4.8; 10263 -5.1; 11289 -7.0; 12418 -8.2; 13660 -9.1; 15026 -8.2; 16529 -7.7; 18182 -7.8; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-A3 Mod GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-A3 Mod ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.44 | 3.2 dB  |
| Peaking | 150 Hz   | 0.58 | -3.4 dB |
| Peaking | 1608 Hz  | 1.44 | -8.7 dB |
| Peaking | 2071 Hz  | 0.63 | 7.4 dB  |
| Peaking | 15076 Hz | 0.75 | -4.2 dB |
| Peaking | 4064 Hz  | 3.42 | 2.9 dB  |
| Peaking | 4736 Hz  | 4.25 | -5.8 dB |
| Peaking | 5591 Hz  | 7.6  | 3.6 dB  |
| Peaking | 9840 Hz  | 3.12 | 1.2 dB  |
| Peaking | 12596 Hz | 3.38 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -5.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20XBA-A3%20Mod/Sony%20XBA-A3%20Mod.png)