# Westone W20
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.1; 25 -5.2; 28 -5.4; 31 -5.5; 34 -5.7; 37 -5.9; 41 -6.1; 45 -6.2; 49 -6.5; 54 -6.7; 60 -7.0; 66 -7.4; 72 -7.8; 79 -8.1; 87 -8.6; 96 -9.0; 106 -9.3; 116 -9.5; 128 -9.9; 141 -10.2; 155 -10.3; 170 -10.5; 187 -10.5; 206 -10.6; 227 -10.5; 249 -10.5; 274 -10.3; 302 -10.2; 332 -9.9; 365 -9.7; 402 -9.4; 442 -9.0; 486 -8.8; 535 -8.4; 588 -7.8; 647 -7.4; 712 -7.2; 783 -6.8; 861 -6.8; 947 -7.0; 1042 -7.2; 1146 -7.3; 1261 -7.5; 1387 -8.0; 1526 -8.5; 1678 -8.9; 1846 -8.9; 2031 -8.7; 2234 -8.3; 2457 -6.7; 2703 -4.5; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.5; 5267 -2.7; 5793 -0.9; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -7.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Westone W20 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.51 | 1.7 dB  |
| Peaking | 197 Hz  | 0.52 | -4.3 dB |
| Peaking | 2086 Hz | 1.54 | -5.0 dB |
| Peaking | 3487 Hz | 1.3  | 7.9 dB  |
| Peaking | 6114 Hz | 5.11 | 4.4 dB  |
| Peaking | 803 Hz  | 3.45 | 0.8 dB  |
| Peaking | 1520 Hz | 5.22 | -0.6 dB |
| Peaking | 3720 Hz | 4.99 | -2.3 dB |
| Peaking | 3936 Hz | 2.19 | 1.6 dB  |
| Peaking | 8438 Hz | 2.56 | -1.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -1.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.7 dB |
| Peaking | 4000 Hz  | 1.41 | 8.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W20/Westone%20W20.png)