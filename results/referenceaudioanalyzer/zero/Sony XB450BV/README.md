# Sony XB450BV
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.6; 25 -3.2; 28 -4.8; 31 -7.1; 34 -9.9; 37 -12.9; 41 -16.7; 45 -20.0; 49 -23.0; 54 -26.1; 60 -27.8; 66 -27.4; 72 -25.9; 79 -23.6; 87 -21.3; 96 -19.5; 106 -17.6; 116 -15.9; 128 -14.7; 141 -13.6; 155 -12.8; 170 -12.4; 187 -12.2; 206 -11.9; 227 -10.8; 249 -9.7; 274 -8.8; 302 -7.8; 332 -6.7; 365 -6.2; 402 -6.1; 442 -6.0; 486 -5.7; 535 -5.4; 588 -5.1; 647 -5.1; 712 -5.1; 783 -5.1; 861 -5.1; 947 -5.0; 1042 -4.8; 1146 -4.6; 1261 -4.5; 1387 -4.3; 1526 -4.1; 1678 -4.2; 1846 -4.2; 2031 -4.5; 2234 -5.3; 2457 -6.3; 2703 -6.8; 2973 -6.0; 3270 -4.0; 3597 -1.3; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -7.9; 6373 -11.7; 7010 -12.0; 7711 -10.4; 8482 -7.0; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XB450BV GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XB450BV ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 1.1  | 12.3 dB  |
| Peaking | 60 Hz   | 0.83 | -24.5 dB |
| Peaking | 675 Hz  | 0.42 | 2.3 dB   |
| Peaking | 4846 Hz | 1.78 | 9.2 dB   |
| Peaking | 6550 Hz | 2.62 | -10.2 dB |
| Peaking | 10 Hz   | 2.1  | 1.3 dB   |
| Peaking | 209 Hz  | 6.21 | -1.3 dB  |
| Peaking | 1918 Hz | 1.99 | 1.9 dB   |
| Peaking | 2708 Hz | 1.81 | -2.9 dB  |
| Peaking | 3591 Hz | 5.3  | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | -25.4 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.6 dB   |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Sony%20XB450BV/Sony%20XB450BV.png)