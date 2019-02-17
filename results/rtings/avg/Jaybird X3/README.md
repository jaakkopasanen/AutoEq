# Jaybird X3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.0; 25 -4.0; 28 -3.9; 31 -3.9; 34 -3.9; 37 -3.9; 41 -3.8; 45 -3.8; 49 -3.8; 54 -3.9; 60 -4.2; 66 -4.5; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.8; 106 -6.3; 116 -6.7; 128 -7.1; 141 -7.3; 155 -7.4; 170 -7.4; 187 -7.5; 206 -7.8; 227 -7.6; 249 -7.2; 274 -6.6; 302 -6.0; 332 -5.5; 365 -5.0; 402 -4.4; 442 -3.8; 486 -3.1; 535 -2.4; 588 -1.8; 647 -1.2; 712 -1.0; 783 -1.1; 861 -1.5; 947 -2.4; 1042 -3.2; 1146 -3.8; 1261 -4.2; 1387 -4.3; 1526 -4.5; 1678 -4.8; 1846 -5.4; 2031 -5.9; 2234 -6.0; 2457 -5.9; 2703 -5.7; 2973 -4.6; 3270 -3.2; 3597 -2.1; 3957 -1.4; 4353 -1.2; 4788 -0.6; 5267 -0.5; 5793 -1.3; 6373 -4.8; 7010 -9.8; 7711 -9.4; 8482 -5.0; 9330 -4.4; 10263 -8.0; 11289 -7.4; 12418 -2.9; 13660 -2.9; 15026 -2.9; 16529 -2.9; 18182 -2.9; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird X3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird X3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 226 Hz   | 0.49 | -7.0 dB  |
| Peaking | 1918 Hz  | 0.17 | 8.1 dB   |
| Peaking | 2041 Hz  | 0.64 | -11.0 dB |
| Peaking | 7302 Hz  | 3.91 | -11.3 dB |
| Peaking | 10719 Hz | 3.1  | -8.1 dB  |
| Peaking | 22 Hz    | 1.54 | -1.0 dB  |
| Peaking | 1169 Hz  | 2.17 | -2.9 dB  |
| Peaking | 1259 Hz  | 0.98 | 1.9 dB   |
| Peaking | 2689 Hz  | 4.08 | -1.5 dB  |
| Peaking | 5237 Hz  | 5.75 | 1.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -4.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20X3/Jaybird%20X3.png)