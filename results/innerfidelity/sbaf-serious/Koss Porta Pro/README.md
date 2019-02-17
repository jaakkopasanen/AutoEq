# Koss Porta Pro
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.5; 34 -2.5; 37 -3.4; 41 -4.4; 45 -5.4; 49 -6.2; 54 -7.2; 60 -8.2; 66 -9.0; 72 -9.8; 79 -10.4; 87 -11.1; 96 -11.6; 106 -12.0; 116 -12.0; 128 -12.2; 141 -12.2; 155 -12.1; 170 -11.9; 187 -11.5; 206 -11.2; 227 -10.8; 249 -10.4; 274 -10.0; 302 -9.7; 332 -9.3; 365 -8.8; 402 -8.4; 442 -7.9; 486 -7.6; 535 -7.3; 588 -6.8; 647 -6.7; 712 -6.5; 783 -6.3; 861 -6.4; 947 -6.5; 1042 -6.5; 1146 -6.7; 1261 -7.1; 1387 -7.9; 1526 -8.9; 1678 -9.9; 1846 -10.4; 2031 -10.0; 2234 -8.7; 2457 -6.3; 2703 -3.9; 2973 -1.4; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -3.5; 4788 -4.9; 5267 -2.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Koss Porta Pro GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Porta Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.86 | 7.1 dB  |
| Peaking | 125 Hz  | 0.55 | -6.3 dB |
| Peaking | 1927 Hz | 2.37 | -5.3 dB |
| Peaking | 3368 Hz | 2.02 | 7.1 dB  |
| Peaking | 6006 Hz | 4.26 | 5.8 dB  |
| Peaking | 807 Hz  | 1.7  | 0.8 dB  |
| Peaking | 1551 Hz | 6.22 | -0.7 dB |
| Peaking | 4607 Hz | 2.93 | 2.0 dB  |
| Peaking | 4641 Hz | 7.54 | -4.0 dB |
| Peaking | 8291 Hz | 3.59 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.7 dB  |
| Peaking | 62 Hz    | 1.41 | -2.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.3 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Porta%20Pro/Koss%20Porta%20Pro.png)