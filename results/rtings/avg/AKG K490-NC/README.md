# AKG K490-NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.9; 60 -1.6; 66 -2.3; 72 -2.9; 79 -3.5; 87 -4.2; 96 -5.0; 106 -5.9; 116 -6.6; 128 -7.2; 141 -7.7; 155 -8.0; 170 -8.2; 187 -8.1; 206 -7.9; 227 -8.1; 249 -8.4; 274 -8.6; 302 -8.6; 332 -8.9; 365 -9.5; 402 -9.8; 442 -10.0; 486 -10.3; 535 -10.4; 588 -10.4; 647 -10.1; 712 -9.5; 783 -8.4; 861 -6.7; 947 -4.8; 1042 -4.1; 1146 -5.2; 1261 -6.9; 1387 -8.2; 1526 -8.7; 1678 -8.2; 1846 -6.7; 2031 -5.5; 2234 -5.5; 2457 -5.0; 2703 -4.6; 2973 -5.6; 3270 -7.1; 3597 -8.7; 3957 -7.3; 4353 -3.4; 4788 -1.5; 5267 -5.1; 5793 -5.3; 6373 -1.3; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -10.1; 12418 -15.1; 13660 -14.0; 15026 -11.1; 16529 -13.0; 18182 -15.0; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K490-NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K490-NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.64 | 6.9 dB  |
| Peaking | 377 Hz   | 0.64 | -3.5 dB |
| Peaking | 6074 Hz  | 1.36 | 3.5 dB  |
| Peaking | 12847 Hz | 2.89 | -8.5 dB |
| Peaking | 17756 Hz | 1.26 | -9.0 dB |
| Peaking | 1029 Hz  | 2.53 | 7.7 dB  |
| Peaking | 1245 Hz  | 0.85 | -4.8 dB |
| Peaking | 2584 Hz  | 1.34 | 4.4 dB  |
| Peaking | 3688 Hz  | 1.98 | -4.6 dB |
| Peaking | 4505 Hz  | 6.94 | 5.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.6 dB   |
| Peaking | 62 Hz    | 1.41 | 4.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.4 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB  |
| Peaking | 500 Hz   | 1.41 | -4.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -10.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K490-NC/AKG%20K490-NC.png)