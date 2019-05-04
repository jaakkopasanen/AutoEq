# Plane Quiet Platinum
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.3; 23 -13.9; 25 -15.1; 28 -16.2; 31 -16.5; 34 -16.3; 37 -15.8; 41 -15.2; 45 -14.7; 49 -14.3; 54 -14.1; 60 -14.0; 66 -13.9; 72 -13.8; 79 -13.7; 87 -13.7; 96 -13.8; 106 -14.0; 116 -14.2; 128 -14.3; 141 -14.3; 155 -14.2; 170 -14.1; 187 -13.8; 206 -13.6; 227 -13.7; 249 -13.5; 274 -12.8; 302 -12.5; 332 -12.1; 365 -11.7; 402 -11.4; 442 -11.2; 486 -11.1; 535 -11.0; 588 -11.0; 647 -11.3; 712 -11.7; 783 -11.8; 861 -11.4; 947 -12.4; 1042 -12.3; 1146 -12.3; 1261 -13.2; 1387 -12.7; 1526 -10.2; 1678 -6.2; 1846 -2.7; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.2; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -7.7; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Plane Quiet Platinum GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Plane Quiet Platinum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 30 Hz   | 1.14 | -7.4 dB  |
| Peaking | 394 Hz  | 0.13 | -10.1 dB |
| Peaking | 1400 Hz | 0.86 | -21.0 dB |
| Peaking | 1836 Hz | 0.42 | 26.6 dB  |
| Peaking | 9741 Hz | 0.93 | -5.2 dB  |
| Peaking | 464 Hz  | 2.39 | 0.6 dB   |
| Peaking | 753 Hz  | 5.33 | -0.8 dB  |
| Peaking | 6165 Hz | 2.57 | 4.1 dB   |
| Peaking | 8019 Hz | 1.1  | -4.5 dB  |
| Peaking | 9729 Hz | 1.98 | 3.8 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -9.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -6.1 dB |
| Peaking | 250 Hz   | 1.41 | -5.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -8.1 dB |
| Peaking | 2000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Plane%20Quiet%20Platinum/Plane%20Quiet%20Platinum.png)