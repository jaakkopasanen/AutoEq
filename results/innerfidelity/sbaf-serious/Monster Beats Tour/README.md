# Monster Beats Tour
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.4; 23 -13.3; 25 -13.2; 28 -13.1; 31 -13.0; 34 -12.9; 37 -12.8; 41 -12.6; 45 -12.5; 49 -12.4; 54 -12.3; 60 -12.1; 66 -12.0; 72 -12.0; 79 -11.9; 87 -11.8; 96 -11.7; 106 -11.5; 116 -11.1; 128 -10.9; 141 -10.7; 155 -10.3; 170 -9.8; 187 -9.4; 206 -8.9; 227 -8.3; 249 -7.8; 274 -7.2; 302 -6.6; 332 -6.0; 365 -5.4; 402 -4.9; 442 -4.2; 486 -3.8; 535 -3.3; 588 -2.6; 647 -2.3; 712 -2.1; 783 -1.8; 861 -2.1; 947 -2.4; 1042 -2.9; 1146 -3.2; 1261 -3.8; 1387 -4.7; 1526 -5.8; 1678 -6.8; 1846 -7.7; 2031 -8.7; 2234 -10.1; 2457 -10.4; 2703 -8.9; 2973 -5.1; 3270 -1.9; 3597 -0.5; 3957 -1.6; 4353 -5.2; 4788 -9.4; 5267 -14.5; 5793 -7.7; 6373 -2.1; 7010 -0.5; 7711 -2.5; 8482 -3.0; 9330 -5.4; 10263 -3.5; 11289 -2.8; 12418 -2.8; 13660 -2.8; 15026 -2.8; 16529 -2.8; 18182 -2.8; 20000 -2.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Monster Beats Tour GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Beats Tour ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.21 | -10.3 dB |
| Peaking | 157 Hz  | 0.8  | -3.9 dB  |
| Peaking | 2367 Hz | 1.93 | -8.6 dB  |
| Peaking | 3512 Hz | 3.16 | 5.6 dB   |
| Peaking | 5201 Hz | 6.08 | -12.5 dB |
| Peaking | 771 Hz  | 1.88 | 1.9 dB   |
| Peaking | 1634 Hz | 4.4  | -1.3 dB  |
| Peaking | 5639 Hz | 7.87 | -2.5 dB  |
| Peaking | 6746 Hz | 4.34 | 4.0 dB   |
| Peaking | 9548 Hz | 7.11 | -3.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.8 dB |
| Peaking | 62 Hz    | 1.41 | -6.5 dB  |
| Peaking | 125 Hz   | 1.41 | -6.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Beats%20Tour/Monster%20Beats%20Tour.png)