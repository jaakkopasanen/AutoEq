# Lear LUF-4F
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.5; 25 -5.7; 28 -6.0; 31 -6.3; 34 -6.5; 37 -6.7; 41 -7.0; 45 -7.3; 49 -7.5; 54 -7.8; 60 -8.2; 66 -8.5; 72 -8.8; 79 -9.1; 87 -9.4; 96 -9.7; 106 -9.8; 116 -9.7; 128 -9.7; 141 -9.4; 155 -9.1; 170 -8.6; 187 -7.9; 206 -7.3; 227 -6.5; 249 -6.0; 274 -5.5; 302 -5.1; 332 -4.9; 365 -4.7; 402 -4.7; 442 -4.6; 486 -4.7; 535 -4.7; 588 -4.5; 647 -4.6; 712 -4.9; 783 -4.9; 861 -5.4; 947 -6.0; 1042 -6.8; 1146 -7.6; 1261 -8.5; 1387 -9.8; 1526 -11.3; 1678 -12.3; 1846 -12.9; 2031 -13.1; 2234 -13.0; 2457 -11.8; 2703 -9.9; 2973 -7.2; 3270 -6.2; 3597 -6.8; 3957 -5.5; 4353 -1.1; 4788 -0.5; 5267 -5.5; 5793 -6.2; 6373 -4.6; 7010 -5.1; 7711 -8.9; 8482 -10.2; 9330 -6.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Lear LUF-4F GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF-4F ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 124 Hz  |  0.71 | -5.6 dB |
| Peaking | 347 Hz  |  0.27 | 3.2 dB  |
| Peaking | 1899 Hz |  1.37 | -8.2 dB |
| Peaking | 4604 Hz |  3.98 | 7.2 dB  |
| Peaking | 8277 Hz |  7.85 | -4.7 dB |
| Peaking | 22 Hz   |  1.6  | 1.5 dB  |
| Peaking | 2432 Hz |  6.61 | -1.3 dB |
| Peaking | 3106 Hz |  7.4  | 2.1 dB  |
| Peaking | 5484 Hz | 10.45 | -2.3 dB |
| Peaking | 6597 Hz |  6.95 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.8 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -8.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF-4F/Lear%20LUF-4F.png)