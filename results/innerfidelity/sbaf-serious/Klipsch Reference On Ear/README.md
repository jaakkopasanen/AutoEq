# Klipsch Reference On Ear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.1; 25 -9.2; 28 -9.3; 31 -9.4; 34 -9.5; 37 -9.6; 41 -9.6; 45 -9.6; 49 -9.6; 54 -9.5; 60 -9.5; 66 -9.6; 72 -9.9; 79 -10.0; 87 -10.2; 96 -10.3; 106 -10.4; 116 -10.5; 128 -10.9; 141 -10.8; 155 -11.0; 170 -10.8; 187 -11.1; 206 -11.2; 227 -11.0; 249 -10.9; 274 -10.5; 302 -10.1; 332 -9.9; 365 -10.1; 402 -9.7; 442 -9.2; 486 -9.7; 535 -9.5; 588 -8.7; 647 -8.2; 712 -7.8; 783 -6.8; 861 -6.1; 947 -5.2; 1042 -4.3; 1146 -3.4; 1261 -2.6; 1387 -3.1; 1526 -3.0; 1678 -3.0; 1846 -2.9; 2031 -2.5; 2234 -2.0; 2457 -1.9; 2703 -2.5; 2973 -3.1; 3270 -3.8; 3597 -4.1; 3957 -4.1; 4353 -3.6; 4788 -1.8; 5267 -0.5; 5793 -1.0; 6373 -2.9; 7010 -4.0; 7711 -6.5; 8482 -8.7; 9330 -8.8; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Klipsch Reference On Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference On Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.8  | -2.1 dB |
| Peaking | 202 Hz  | 0.29 | -4.4 dB |
| Peaking | 1234 Hz | 1.45 | 4.0 dB  |
| Peaking | 2398 Hz | 1.5  | 4.0 dB  |
| Peaking | 5392 Hz | 3.18 | 6.1 dB  |
| Peaking | 455 Hz  | 2.96 | 1.1 dB  |
| Peaking | 500 Hz  | 4.06 | -1.4 dB |
| Peaking | 6827 Hz | 6.12 | 1.9 dB  |
| Peaking | 8850 Hz | 3.86 | -3.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Reference%20On%20Ear/Klipsch%20Reference%20On%20Ear.png)