# Philips O'Neil Bend
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.9; 25 -4.5; 28 -5.1; 31 -5.6; 34 -6.1; 37 -6.6; 41 -7.0; 45 -7.4; 49 -7.8; 54 -8.2; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.6; 87 -10.1; 96 -10.4; 106 -10.6; 116 -10.7; 128 -10.7; 141 -11.1; 155 -11.3; 170 -10.7; 187 -10.8; 206 -10.6; 227 -10.2; 249 -9.8; 274 -9.1; 302 -8.5; 332 -7.9; 365 -7.5; 402 -7.2; 442 -6.9; 486 -6.8; 535 -6.9; 588 -6.7; 647 -6.7; 712 -6.8; 783 -6.7; 861 -6.9; 947 -6.7; 1042 -6.5; 1146 -5.9; 1261 -5.2; 1387 -4.8; 1526 -4.1; 1678 -3.5; 1846 -2.5; 2031 -1.4; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.9; 4788 -1.3; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips O'Neil Bend GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips O'Neil Bend ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.19 | 4.4 dB  |
| Peaking | 99 Hz   | 0.66 | -3.1 dB |
| Peaking | 189 Hz  | 1.02 | -2.7 dB |
| Peaking | 2794 Hz | 1.03 | 6.5 dB  |
| Peaking | 5647 Hz | 2.83 | 4.8 dB  |
| Peaking | 952 Hz  | 2.87 | -1.0 dB |
| Peaking | 2147 Hz | 3.15 | 1.1 dB  |
| Peaking | 2763 Hz | 2.86 | -1.1 dB |
| Peaking | 3857 Hz | 4.93 | 1.1 dB  |
| Peaking | 8403 Hz | 3.47 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20O'Neil%20Bend/Philips%20O'Neil%20Bend.png)