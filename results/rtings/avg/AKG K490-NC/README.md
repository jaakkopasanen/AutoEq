# AKG K490-NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.6; 54 -1.0; 60 -1.8; 66 -2.5; 72 -3.1; 79 -3.8; 87 -4.5; 96 -5.3; 106 -6.1; 116 -6.9; 128 -7.5; 141 -7.9; 155 -8.2; 170 -8.4; 187 -8.3; 206 -8.0; 227 -8.2; 249 -8.4; 274 -8.6; 302 -8.7; 332 -9.0; 365 -9.7; 402 -9.9; 442 -10.1; 486 -10.3; 535 -10.4; 588 -10.3; 647 -10.0; 712 -9.4; 783 -8.3; 861 -6.6; 947 -4.7; 1042 -4.0; 1146 -5.1; 1261 -6.7; 1387 -8.1; 1526 -8.5; 1678 -7.9; 1846 -6.4; 2031 -5.0; 2234 -4.6; 2457 -4.1; 2703 -4.1; 2973 -5.7; 3270 -7.4; 3597 -8.9; 3957 -7.6; 4353 -3.7; 4788 -0.9; 5267 -4.8; 5793 -5.4; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -9.2; 12418 -15.0; 13660 -14.7; 15026 -11.5; 16529 -13.3; 18182 -15.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K490-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K490-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.62 | 6.8 dB  |
| Peaking | 342 Hz   | 0.58 | -3.5 dB |
| Peaking | 5967 Hz  | 1.22 | 3.4 dB  |
| Peaking | 12913 Hz | 2.9  | -8.8 dB |
| Peaking | 17893 Hz | 1.29 | -9.0 dB |
| Peaking | 619 Hz   | 2.65 | -1.8 dB |
| Peaking | 1011 Hz  | 4.35 | 4.4 dB  |
| Peaking | 2603 Hz  | 2.22 | 7.7 dB  |
| Peaking | 3144 Hz  | 1.1  | -6.0 dB |
| Peaking | 4665 Hz  | 6.78 | 6.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.6 dB  |
| Peaking | 250 Hz   | 1.41 | -1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -4.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -10.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K490-NC/AKG%20K490-NC.png)