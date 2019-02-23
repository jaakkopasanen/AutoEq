# Klipsch Image S4i
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.1; 23 -12.1; 25 -12.1; 28 -12.1; 31 -12.2; 34 -12.2; 37 -12.2; 41 -12.2; 45 -12.3; 49 -12.4; 54 -12.7; 60 -12.8; 66 -13.0; 72 -13.2; 79 -13.4; 87 -13.5; 96 -13.7; 106 -13.7; 116 -13.7; 128 -13.7; 141 -13.7; 155 -13.6; 170 -13.4; 187 -13.1; 206 -12.7; 227 -12.3; 249 -11.8; 274 -11.2; 302 -10.5; 332 -9.8; 365 -9.0; 402 -8.3; 442 -7.5; 486 -6.7; 535 -5.9; 588 -5.1; 647 -4.5; 712 -3.8; 783 -3.4; 861 -3.3; 947 -3.3; 1042 -3.6; 1146 -3.9; 1261 -4.3; 1387 -4.8; 1526 -5.4; 1678 -5.6; 1846 -5.2; 2031 -5.2; 2234 -5.0; 2457 -4.6; 2703 -4.2; 2973 -3.3; 3270 -1.4; 3597 -0.5; 3957 -0.5; 4353 -2.2; 4788 -3.8; 5267 -5.3; 5793 -7.9; 6373 -6.7; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Image S4i GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Image S4i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.7  | -4.0 dB |
| Peaking | 47 Hz   | 0.34 | -3.9 dB |
| Peaking | 171 Hz  | 0.48 | -5.4 dB |
| Peaking | 795 Hz  | 0.94 | 4.3 dB  |
| Peaking | 3694 Hz | 2.46 | 6.4 dB  |
| Peaking | 1584 Hz | 7.96 | -0.5 dB |
| Peaking | 5021 Hz | 2.72 | 1.7 dB  |
| Peaking | 5951 Hz | 3.07 | -3.7 dB |
| Peaking | 6866 Hz | 7.31 | 3.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Image%20S4i/Klipsch%20Image%20S4i.png)