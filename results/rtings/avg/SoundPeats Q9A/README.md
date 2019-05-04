# SoundPeats Q9A
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.4; 23 -12.5; 25 -12.5; 28 -12.5; 31 -12.5; 34 -12.5; 37 -12.6; 41 -12.6; 45 -12.6; 49 -12.6; 54 -12.7; 60 -12.8; 66 -12.9; 72 -13.0; 79 -13.1; 87 -13.3; 96 -13.4; 106 -13.4; 116 -13.3; 128 -13.4; 141 -13.5; 155 -13.4; 170 -13.1; 187 -12.8; 206 -12.4; 227 -11.9; 249 -11.4; 274 -10.8; 302 -10.1; 332 -9.5; 365 -8.8; 402 -8.0; 442 -7.2; 486 -6.3; 535 -5.3; 588 -4.4; 647 -3.5; 712 -3.0; 783 -2.6; 861 -2.4; 947 -2.2; 1042 -2.4; 1146 -2.9; 1261 -3.5; 1387 -4.7; 1526 -6.4; 1678 -8.3; 1846 -9.5; 2031 -9.5; 2234 -7.9; 2457 -5.0; 2703 -2.3; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.9; 4353 -2.5; 4788 -4.9; 5267 -6.8; 5793 -6.0; 6373 -3.4; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats Q9A GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats Q9A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.22 | -5.5 dB |
| Peaking | 166 Hz  | 0.4  | -6.4 dB |
| Peaking | 899 Hz  | 0.64 | 6.1 dB  |
| Peaking | 1935 Hz | 1.86 | -7.9 dB |
| Peaking | 3202 Hz | 1.59 | 7.3 dB  |
| Peaking | 616 Hz  | 3.7  | 0.1 dB  |
| Peaking | 4148 Hz | 5.58 | 1.7 dB  |
| Peaking | 5367 Hz | 3.99 | -2.5 dB |
| Peaking | 6592 Hz | 4.36 | 4.5 dB  |
| Peaking | 7047 Hz | 1.52 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.0 dB |
| Peaking | 62 Hz    | 1.41 | -4.5 dB |
| Peaking | 125 Hz   | 1.41 | -5.9 dB |
| Peaking | 250 Hz   | 1.41 | -4.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20Q9A/SoundPeats%20Q9A.png)