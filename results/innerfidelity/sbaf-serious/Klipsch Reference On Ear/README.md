# Klipsch Reference On Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.6; 23 -10.8; 25 -10.9; 28 -11.1; 31 -11.2; 34 -11.3; 37 -11.3; 41 -11.3; 45 -11.4; 49 -11.3; 54 -11.3; 60 -11.3; 66 -11.4; 72 -11.6; 79 -11.7; 87 -11.9; 96 -12.1; 106 -12.2; 116 -12.3; 128 -12.6; 141 -12.5; 155 -12.8; 170 -12.6; 187 -12.9; 206 -13.0; 227 -12.8; 249 -12.6; 274 -12.2; 302 -11.8; 332 -11.7; 365 -11.9; 402 -11.4; 442 -10.9; 486 -11.5; 535 -11.2; 588 -10.5; 647 -10.0; 712 -9.5; 783 -8.6; 861 -7.9; 947 -7.0; 1042 -6.1; 1146 -5.1; 1261 -4.4; 1387 -4.8; 1526 -4.7; 1678 -4.7; 1846 -4.6; 2031 -4.3; 2234 -3.8; 2457 -3.7; 2703 -4.3; 2973 -4.9; 3270 -5.6; 3597 -5.8; 3957 -5.9; 4353 -5.4; 4788 -3.6; 5267 -0.5; 5793 -2.3; 6373 -4.7; 7010 -5.4; 7711 -8.1; 8482 -10.4; 9330 -10.6; 10263 -7.5; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.25 | -4.1 dB |
| Peaking | 223 Hz  | 0.53 | -5.0 dB |
| Peaking | 603 Hz  | 1.01 | -4.1 dB |
| Peaking | 1411 Hz | 0.35 | 3.1 dB  |
| Peaking | 2458 Hz | 5.23 | 0.9 dB  |
| Peaking | 4132 Hz | 1.61 | -2.1 dB |
| Peaking | 5352 Hz | 3.67 | 6.4 dB  |
| Peaking | 8854 Hz | 3.63 | -5.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.4 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20On%20Ear/Klipsch%20Reference%20On%20Ear.png)