# Grado RS1e S Cushions
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.3; 37 -2.0; 41 -3.0; 45 -3.8; 49 -4.6; 54 -5.4; 60 -6.3; 66 -7.0; 72 -7.6; 79 -8.2; 87 -8.9; 96 -9.4; 106 -9.8; 116 -10.0; 128 -10.2; 141 -10.4; 155 -10.5; 170 -10.4; 187 -10.3; 206 -10.0; 227 -9.7; 249 -9.5; 274 -9.4; 302 -9.3; 332 -8.9; 365 -8.5; 402 -8.2; 442 -7.8; 486 -7.6; 535 -7.4; 588 -6.9; 647 -6.7; 712 -6.7; 783 -6.4; 861 -6.5; 947 -6.4; 1042 -6.4; 1146 -6.4; 1261 -6.1; 1387 -6.1; 1526 -5.4; 1678 -7.4; 1846 -13.2; 2031 -12.5; 2234 -9.8; 2457 -6.5; 2703 -3.7; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Grado RS1e S Cushions GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e S Cushions ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.55 | 7.9 dB   |
| Peaking | 130 Hz  |  0.31 | -5.6 dB  |
| Peaking | 696 Hz  |  0.22 | 1.3 dB   |
| Peaking | 1988 Hz |  3.61 | -10.2 dB |
| Peaking | 4057 Hz |  0.98 | 6.6 dB   |
| Peaking | 1611 Hz |  7.53 | 2.9 dB   |
| Peaking | 1774 Hz | 10.35 | -2.6 dB  |
| Peaking | 6263 Hz |  2.99 | 5.3 dB   |
| Peaking | 7183 Hz |  1.39 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 9.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20S%20Cushions/Grado%20RS1e%20S%20Cushions.png)