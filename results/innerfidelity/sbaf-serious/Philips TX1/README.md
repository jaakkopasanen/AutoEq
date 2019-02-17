# Philips TX1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.8; 28 -13.8; 31 -13.7; 34 -13.6; 37 -13.5; 41 -13.4; 45 -13.4; 49 -13.3; 54 -13.2; 60 -13.2; 66 -13.2; 72 -13.2; 79 -13.2; 87 -13.2; 96 -13.2; 106 -13.0; 116 -12.8; 128 -12.5; 141 -12.3; 155 -12.0; 170 -11.6; 187 -11.2; 206 -10.7; 227 -10.2; 249 -9.7; 274 -9.2; 302 -8.6; 332 -8.1; 365 -7.5; 402 -7.0; 442 -6.4; 486 -5.9; 535 -5.5; 588 -4.8; 647 -4.6; 712 -4.5; 783 -4.1; 861 -4.3; 947 -4.6; 1042 -5.0; 1146 -5.3; 1261 -5.8; 1387 -6.5; 1526 -7.2; 1678 -7.7; 1846 -7.7; 2031 -7.4; 2234 -6.7; 2457 -5.1; 2703 -3.8; 2973 -1.9; 3270 -0.8; 3597 -0.5; 3957 -2.1; 4353 -5.5; 4788 -8.0; 5267 -8.9; 5793 -7.6; 6373 -5.8; 7010 -4.4; 7711 -4.6; 8482 -6.0; 9330 -6.5; 10263 -5.7; 11289 -4.9; 12418 -4.9; 13660 -4.9; 15026 -4.9; 16529 -4.9; 18182 -4.9; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips TX1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips TX1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.2  | -8.7 dB |
| Peaking | 158 Hz  | 0.75 | -3.8 dB |
| Peaking | 1879 Hz | 2.25 | -3.6 dB |
| Peaking | 3506 Hz | 2.24 | 5.9 dB  |
| Peaking | 5142 Hz | 2.96 | -5.6 dB |
| Peaking | 317 Hz  | 2.07 | -0.7 dB |
| Peaking | 734 Hz  | 1.5  | 1.4 dB  |
| Peaking | 1449 Hz | 4.08 | -0.8 dB |
| Peaking | 7221 Hz | 5.07 | 1.6 dB  |
| Peaking | 9159 Hz | 4.05 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB |
| Peaking | 62 Hz    | 1.41 | -6.0 dB |
| Peaking | 125 Hz   | 1.41 | -6.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.8 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20TX1/Philips%20TX1.png)