# Syun Mix1 Gold
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -8.2; 25 -8.6; 28 -9.2; 31 -9.6; 34 -10.0; 37 -10.4; 41 -10.8; 45 -11.2; 49 -11.5; 54 -11.9; 60 -12.3; 66 -12.6; 72 -12.9; 79 -13.3; 87 -13.6; 96 -14.0; 106 -14.2; 116 -14.3; 128 -14.5; 141 -14.5; 155 -14.5; 170 -14.3; 187 -14.1; 206 -13.9; 227 -13.4; 249 -13.1; 274 -12.6; 302 -12.1; 332 -11.5; 365 -10.9; 402 -10.2; 442 -9.4; 486 -8.9; 535 -8.2; 588 -7.2; 647 -6.6; 712 -6.1; 783 -5.5; 861 -5.2; 947 -5.0; 1042 -4.4; 1146 -3.9; 1261 -4.2; 1387 -4.9; 1526 -5.4; 1678 -5.6; 1846 -5.6; 2031 -5.1; 2234 -4.8; 2457 -4.0; 2703 -3.1; 2973 -2.1; 3270 -1.3; 3597 -1.6; 3957 -3.3; 4353 -6.0; 4788 -5.5; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Syun Mix1 Gold GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun Mix1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 62 Hz   | 0.48 | -3.1 dB |
| Peaking | 182 Hz  | 0.45 | -6.7 dB |
| Peaking | 961 Hz  | 0.93 | 3.0 dB  |
| Peaking | 3229 Hz | 2.8  | 5.1 dB  |
| Peaking | 5952 Hz | 4.04 | 6.4 dB  |
| Peaking | 1207 Hz | 5.59 | 0.8 dB  |
| Peaking | 1571 Hz | 2.7  | -0.6 dB |
| Peaking | 4528 Hz | 5.5  | -4.2 dB |
| Peaking | 4652 Hz | 2    | 2.1 dB  |
| Peaking | 8241 Hz | 3.11 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.8 dB |
| Peaking | 250 Hz   | 1.41 | -5.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.3 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20Mix1%20Gold/Syun%20Mix1%20Gold.png)