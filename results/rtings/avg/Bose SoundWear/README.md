# Bose SoundWear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.2; 106 -1.5; 116 -1.4; 128 -1.6; 141 -2.7; 155 -4.1; 170 -5.4; 187 -5.4; 206 -4.5; 227 -1.4; 249 -3.3; 274 -4.5; 302 -6.0; 332 -7.1; 365 -6.1; 402 -9.6; 442 -9.5; 486 -9.9; 535 -11.6; 588 -10.1; 647 -7.4; 712 -8.8; 783 -10.1; 861 -9.9; 947 -8.0; 1042 -6.3; 1146 -7.0; 1261 -9.2; 1387 -4.3; 1526 -2.9; 1678 -3.2; 1846 -6.8; 2031 -10.4; 2234 -11.2; 2457 -9.9; 2703 -10.4; 2973 -11.6; 3270 -14.5; 3597 -15.4; 3957 -13.7; 4353 -15.7; 4788 -14.9; 5267 -14.4; 5793 -8.8; 6373 -8.4; 7010 -5.3; 7711 -6.4; 8482 -10.3; 9330 -11.3; 10263 -8.6; 11289 -10.4; 12418 -16.0; 13660 -18.9; 15026 -18.7; 16529 -13.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundWear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundWear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.22 | 6.2 dB   |
| Peaking | 519 Hz   | 1.62 | -5.0 dB  |
| Peaking | 3461 Hz  | 2.17 | -7.5 dB  |
| Peaking | 4757 Hz  | 3.83 | -6.7 dB  |
| Peaking | 14303 Hz | 1.59 | -14.1 dB |
| Peaking | 180 Hz   | 4.2  | -2.7 dB  |
| Peaking | 234 Hz   | 6.13 | 3.5 dB   |
| Peaking | 1597 Hz  | 4.5  | 9.3 dB   |
| Peaking | 2060 Hz  | 1.24 | -5.5 dB  |
| Peaking | 2747 Hz  | 1.49 | 3.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB   |
| Peaking | 62 Hz    | 1.41 | 5.2 dB   |
| Peaking | 125 Hz   | 1.41 | 3.0 dB   |
| Peaking | 250 Hz   | 1.41 | 2.6 dB   |
| Peaking | 500 Hz   | 1.41 | -4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | -9.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.5 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundWear/Bose%20SoundWear.png)