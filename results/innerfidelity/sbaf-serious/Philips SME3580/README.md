# Philips SME3580
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.0; 23 -13.8; 25 -13.6; 28 -13.3; 31 -13.0; 34 -12.6; 37 -12.3; 41 -12.0; 45 -11.6; 49 -11.4; 54 -11.1; 60 -10.8; 66 -10.5; 72 -10.3; 79 -10.1; 87 -9.9; 96 -9.7; 106 -9.4; 116 -9.0; 128 -8.8; 141 -8.4; 155 -8.0; 170 -7.6; 187 -7.1; 206 -6.6; 227 -6.1; 249 -5.6; 274 -5.0; 302 -4.5; 332 -3.9; 365 -3.4; 402 -3.0; 442 -2.3; 486 -2.0; 535 -1.6; 588 -1.0; 647 -0.8; 712 -0.7; 783 -0.5; 861 -0.6; 947 -0.9; 1042 -1.5; 1146 -2.1; 1261 -3.0; 1387 -4.1; 1526 -5.2; 1678 -6.2; 1846 -6.8; 2031 -7.5; 2234 -8.6; 2457 -9.2; 2703 -8.4; 2973 -5.4; 3270 -2.2; 3597 -0.6; 3957 -1.5; 4353 -4.6; 4788 -7.9; 5267 -9.0; 5793 -5.7; 6373 -2.2; 7010 -1.8; 7711 -4.0; 8482 -4.3; 9330 -4.3; 10263 -4.3; 11289 -4.3; 12418 -4.3; 13660 -4.3; 15026 -4.3; 16529 -4.3; 18182 -4.3; 20000 -4.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Philips SME3580 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips SME3580 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.55 | -8.7 dB |
| Peaking | 95 Hz    | 0.48 | -4.1 dB |
| Peaking | 700 Hz   | 0.81 | 4.3 dB  |
| Peaking | 2218 Hz  | 2.47 | -5.6 dB |
| Peaking | 22050 Hz | 2.36 | -2.2 dB |
| Peaking | 1603 Hz  | 5.15 | -1.6 dB |
| Peaking | 2719 Hz  | 4.55 | -4.1 dB |
| Peaking | 3682 Hz  | 1.82 | 6.5 dB  |
| Peaking | 5095 Hz  | 2.5  | -7.6 dB |
| Peaking | 6618 Hz  | 4.87 | 5.0 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.6 dB |
| Peaking | 62 Hz    | 1.41 | -4.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 2.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.9 dB |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20SME3580/Philips%20SME3580.png)