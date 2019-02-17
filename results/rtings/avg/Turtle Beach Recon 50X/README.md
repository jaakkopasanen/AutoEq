# Turtle Beach Recon 50X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.1; 25 -4.2; 28 -4.5; 31 -4.7; 34 -4.9; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.8; 54 -4.8; 60 -5.0; 66 -5.5; 72 -5.9; 79 -6.5; 87 -7.1; 96 -7.5; 106 -7.9; 116 -8.4; 128 -9.1; 141 -9.9; 155 -10.5; 170 -10.9; 187 -10.9; 206 -11.0; 227 -11.2; 249 -11.6; 274 -12.0; 302 -11.9; 332 -12.0; 365 -12.0; 402 -11.2; 442 -11.0; 486 -11.1; 535 -11.0; 588 -10.9; 647 -10.6; 712 -9.8; 783 -8.5; 861 -7.3; 947 -6.6; 1042 -6.5; 1146 -6.3; 1261 -6.1; 1387 -5.3; 1526 -4.3; 1678 -3.9; 1846 -3.6; 2031 -3.5; 2234 -3.1; 2457 -2.4; 2703 -3.2; 2973 -4.8; 3270 -5.3; 3597 -5.1; 3957 -4.7; 4353 -3.0; 4788 -0.7; 5267 -0.5; 5793 -0.6; 6373 -5.7; 7010 -7.3; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Turtle Beach Recon 50X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Turtle Beach Recon 50X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 33 Hz   |  0.33 | 2.5 dB  |
| Peaking | 253 Hz  |  0.52 | -5.7 dB |
| Peaking | 596 Hz  |  2.42 | -2.1 dB |
| Peaking | 2049 Hz |  1.16 | 3.8 dB  |
| Peaking | 5180 Hz |  3.7  | 6.5 dB  |
| Peaking | 726 Hz  |  4.84 | -0.8 dB |
| Peaking | 917 Hz  |  2.35 | 1.0 dB  |
| Peaking | 1221 Hz |  3.38 | -0.5 dB |
| Peaking | 5890 Hz | 10.25 | 3.2 dB  |
| Peaking | 6700 Hz |  3.99 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | -4.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Turtle%20Beach%20Recon%2050X/Turtle%20Beach%20Recon%2050X.png)