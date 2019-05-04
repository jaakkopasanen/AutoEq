# SoundPeats TrueFree
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -17.1; 23 -16.8; 25 -16.5; 28 -16.1; 31 -15.7; 34 -15.3; 37 -15.0; 41 -14.5; 45 -14.1; 49 -13.8; 54 -13.4; 60 -13.0; 66 -12.8; 72 -12.6; 79 -12.4; 87 -12.3; 96 -12.2; 106 -12.1; 116 -12.0; 128 -11.9; 141 -11.6; 155 -11.3; 170 -10.9; 187 -10.5; 206 -10.0; 227 -9.5; 249 -9.0; 274 -8.6; 302 -8.1; 332 -7.6; 365 -7.1; 402 -6.7; 442 -6.2; 486 -5.8; 535 -5.2; 588 -4.8; 647 -4.3; 712 -3.9; 783 -3.5; 861 -3.5; 947 -3.7; 1042 -4.3; 1146 -5.3; 1261 -6.1; 1387 -6.7; 1526 -7.3; 1678 -7.9; 1846 -8.5; 2031 -8.7; 2234 -8.4; 2457 -7.7; 2703 -7.5; 2973 -6.5; 3270 -4.4; 3597 -2.8; 3957 -2.0; 4353 -1.6; 4788 -1.4; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.7; 8482 -7.1; 9330 -7.5; 10263 -11.0; 11289 -11.4; 12418 -6.7; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -9.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats TrueFree GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats TrueFree ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.28 | -10.6 dB |
| Peaking | 141 Hz   | 0.78 | -3.5 dB  |
| Peaking | 755 Hz   | 1.93 | 3.5 dB   |
| Peaking | 5313 Hz  | 1.83 | 6.7 dB   |
| Peaking | 10722 Hz | 3.34 | -6.2 dB  |
| Peaking | 1018 Hz  | 3.46 | 1.4 dB   |
| Peaking | 2116 Hz  | 1.39 | -2.9 dB  |
| Peaking | 3702 Hz  | 3.77 | 2.8 dB   |
| Peaking | 7940 Hz  | 9.72 | -1.8 dB  |
| Peaking | 18218 Hz | 2.54 | -3.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -10.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.9 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -2.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.4 dB   |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -1.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/SoundPeats%20TrueFree/SoundPeats%20TrueFree.png)