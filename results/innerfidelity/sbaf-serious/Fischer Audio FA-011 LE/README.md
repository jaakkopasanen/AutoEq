# Fischer Audio FA-011 LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.5; 23 -2.5; 25 -3.4; 28 -4.6; 31 -5.7; 34 -6.6; 37 -7.4; 41 -8.1; 45 -8.7; 49 -9.1; 54 -9.5; 60 -9.7; 66 -9.9; 72 -9.9; 79 -10.1; 87 -10.2; 96 -10.3; 106 -10.3; 116 -10.2; 128 -10.2; 141 -10.1; 155 -10.1; 170 -10.1; 187 -9.5; 206 -9.8; 227 -9.7; 249 -9.7; 274 -9.4; 302 -9.6; 332 -9.6; 365 -9.6; 402 -9.6; 442 -9.5; 486 -9.5; 535 -9.6; 588 -9.2; 647 -8.5; 712 -7.9; 783 -7.8; 861 -8.2; 947 -8.0; 1042 -7.4; 1146 -6.7; 1261 -5.8; 1387 -5.4; 1526 -5.3; 1678 -5.0; 1846 -4.3; 2031 -3.3; 2234 -2.5; 2457 -2.0; 2703 -1.6; 2973 -1.1; 3270 -0.5; 3597 -1.1; 3957 -1.6; 4353 -2.5; 4788 -1.0; 5267 -2.4; 5793 -2.5; 6373 -3.2; 7010 -4.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio FA-011 LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-011 LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 1.03 | 7.2 dB  |
| Peaking | 73 Hz    | 0.32 | -4.1 dB |
| Peaking | 501 Hz   | 0.69 | -2.4 dB |
| Peaking | 2978 Hz  | 1.06 | 5.6 dB  |
| Peaking | 5227 Hz  | 2.48 | 2.9 dB  |
| Peaking | 965 Hz   | 3.32 | -1.9 dB |
| Peaking | 990 Hz   | 1.66 | 1.2 dB  |
| Peaking | 6462 Hz  | 5.67 | 1.5 dB  |
| Peaking | 8402 Hz  | 1.36 | -1.0 dB |
| Peaking | 17803 Hz | 3.47 | -1.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -3.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20FA-011%20LE/Fischer%20Audio%20FA-011%20LE.png)