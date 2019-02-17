# Panasonic RP HT600 S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -5.6; 25 -6.6; 28 -7.9; 31 -8.8; 34 -9.5; 37 -10.0; 41 -10.4; 45 -10.5; 49 -10.6; 54 -10.7; 60 -10.6; 66 -10.6; 72 -10.6; 79 -10.7; 87 -10.7; 96 -10.9; 106 -10.8; 116 -10.5; 128 -10.8; 141 -11.1; 155 -11.4; 170 -11.2; 187 -11.3; 206 -11.5; 227 -11.5; 249 -11.6; 274 -11.7; 302 -11.8; 332 -11.7; 365 -11.8; 402 -11.8; 442 -11.7; 486 -11.8; 535 -11.9; 588 -11.4; 647 -11.0; 712 -10.6; 783 -9.9; 861 -8.7; 947 -7.0; 1042 -6.4; 1146 -6.4; 1261 -7.9; 1387 -10.4; 1526 -12.5; 1678 -12.9; 1846 -12.3; 2031 -9.9; 2234 -8.3; 2457 -6.6; 2703 -4.8; 2973 -3.3; 3270 -2.6; 3597 -2.8; 3957 -0.6; 4353 -1.1; 4788 -3.2; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -10.1; 9330 -13.2; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Panasonic RP HT600 S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic RP HT600 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 189 Hz  | 0.23 | -5.2 dB |
| Peaking | 1747 Hz | 3.12 | -6.9 dB |
| Peaking | 3798 Hz | 1.28 | 4.9 dB  |
| Peaking | 5997 Hz | 2.77 | 5.0 dB  |
| Peaking | 9167 Hz | 4.78 | -8.3 dB |
| Peaking | 17 Hz   | 0.21 | 6.1 dB  |
| Peaking | 39 Hz   | 0.71 | -6.6 dB |
| Peaking | 756 Hz  | 0.82 | -2.5 dB |
| Peaking | 1035 Hz | 1.86 | 4.8 dB  |
| Peaking | 1427 Hz | 5.84 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | -5.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 8.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.0 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20RP%20HT600%20S/Panasonic%20RP%20HT600%20S.png)