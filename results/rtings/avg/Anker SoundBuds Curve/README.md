# Anker SoundBuds Curve
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.7; 23 -14.5; 25 -14.4; 28 -14.1; 31 -13.7; 34 -13.3; 37 -12.9; 41 -12.4; 45 -12.0; 49 -11.6; 54 -11.1; 60 -10.7; 66 -10.4; 72 -10.3; 79 -10.1; 87 -10.1; 96 -10.2; 106 -10.3; 116 -10.4; 128 -10.5; 141 -10.2; 155 -9.6; 170 -8.6; 187 -7.1; 206 -5.0; 227 -2.8; 249 -1.8; 274 -2.2; 302 -2.8; 332 -3.1; 365 -3.3; 402 -3.2; 442 -3.1; 486 -3.0; 535 -2.7; 588 -2.3; 647 -1.7; 712 -1.0; 783 -0.5; 861 -0.5; 947 -0.9; 1042 -1.3; 1146 -1.7; 1261 -1.9; 1387 -2.0; 1526 -2.0; 1678 -2.2; 1846 -2.5; 2031 -2.9; 2234 -3.1; 2457 -3.1; 2703 -3.4; 2973 -3.9; 3270 -4.1; 3597 -4.0; 3957 -4.2; 4353 -5.0; 4788 -6.5; 5267 -7.7; 5793 -7.6; 6373 -5.1; 7010 -3.0; 7711 -3.7; 8482 -4.0; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -4.0; 13660 -4.0; 15026 -4.0; 16529 -4.0; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Anker SoundBuds Curve GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Anker SoundBuds Curve ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 19 Hz   | 0.27 | -10.7 dB |
| Peaking | 114 Hz  | 1.55 | -4.0 dB  |
| Peaking | 157 Hz  | 2.83 | -3.8 dB  |
| Peaking | 431 Hz  | 0.2  | 2.6 dB   |
| Peaking | 5302 Hz | 3.52 | -4.6 dB  |
| Peaking | 251 Hz  | 3.65 | 2.7 dB   |
| Peaking | 445 Hz  | 0.67 | -1.7 dB  |
| Peaking | 814 Hz  | 1.85 | 2.2 dB   |
| Peaking | 3085 Hz | 3.03 | -0.6 dB  |
| Peaking | 7167 Hz | 8.4  | 1.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -11.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -6.8 dB  |
| Peaking | 250 Hz   | 1.41 | 2.3 dB   |
| Peaking | 500 Hz   | 1.41 | 0.7 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | -1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.1 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Anker%20SoundBuds%20Curve/Anker%20SoundBuds%20Curve.png)