# Pioneer HDJ-2000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.6; 49 -1.6; 54 -3.3; 60 -5.0; 66 -6.3; 72 -7.4; 79 -8.5; 87 -9.6; 96 -10.1; 106 -10.3; 116 -10.0; 128 -9.9; 141 -9.9; 155 -10.0; 170 -9.7; 187 -9.7; 206 -9.8; 227 -9.7; 249 -9.7; 274 -9.5; 302 -9.2; 332 -9.1; 365 -8.9; 402 -8.9; 442 -8.6; 486 -8.4; 535 -8.5; 588 -8.4; 647 -8.4; 712 -8.8; 783 -8.7; 861 -8.3; 947 -7.8; 1042 -8.2; 1146 -8.9; 1261 -8.8; 1387 -9.2; 1526 -9.4; 1678 -9.2; 1846 -8.5; 2031 -6.9; 2234 -4.6; 2457 -2.4; 2703 -1.3; 2973 -0.9; 3270 -2.1; 3597 -4.3; 3957 -7.1; 4353 -5.4; 4788 -0.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -7.8; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer HDJ-2000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 45 Hz    |  0.41 | 17.0 dB  |
| Peaking | 79 Hz    |  0.4  | -14.9 dB |
| Peaking | 2813 Hz  |  1.78 | 12.5 dB  |
| Peaking | 3256 Hz  |  0.46 | -7.9 dB  |
| Peaking | 5568 Hz  |  1.79 | 11.1 dB  |
| Peaking | 968 Hz   |  7.71 | 1.1 dB   |
| Peaking | 2310 Hz  |  9.7  | 1.1 dB   |
| Peaking | 4060 Hz  | 12.1  | -2.7 dB  |
| Peaking | 9735 Hz  |  5.17 | -2.0 dB  |
| Peaking | 11345 Hz |  0.81 | 0.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 8.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB |
| Peaking | 2000 Hz  | 1.41 | -0.2 dB |
| Peaking | 4000 Hz  | 1.41 | 4.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-2000/Pioneer%20HDJ-2000.png)