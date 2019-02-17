# AKG K712 PRO
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.8; 31 -2.2; 34 -2.5; 37 -2.8; 41 -3.1; 45 -3.4; 49 -3.6; 54 -3.9; 60 -4.2; 66 -4.6; 72 -4.9; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.6; 116 -7.1; 128 -7.5; 141 -7.9; 155 -8.2; 170 -8.3; 187 -8.4; 206 -8.4; 227 -8.4; 249 -8.5; 274 -8.5; 302 -8.6; 332 -8.6; 365 -8.6; 402 -8.6; 442 -8.6; 486 -8.6; 535 -8.0; 588 -7.9; 647 -7.8; 712 -7.4; 783 -6.6; 861 -5.4; 947 -4.6; 1042 -4.0; 1146 -4.2; 1261 -4.7; 1387 -5.3; 1526 -6.2; 1678 -7.8; 1846 -9.8; 2031 -11.2; 2234 -11.0; 2457 -8.7; 2703 -6.3; 2973 -4.4; 3270 -5.4; 3597 -7.4; 3957 -8.6; 4353 -8.6; 4788 -7.0; 5267 -6.3; 5793 -7.3; 6373 -8.8; 7010 -9.5; 7711 -10.6; 8482 -11.4; 9330 -7.4; 10263 -4.1; 11289 -4.1; 12418 -5.0; 13660 -5.9; 15026 -4.6; 16529 -9.5; 18182 -15.7; 20000 -13.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K712 PRO GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K712 PRO ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 280 Hz   | 0.5  | -5.0 dB  |
| Peaking | 2082 Hz  | 3.4  | -7.4 dB  |
| Peaking | 4166 Hz  | 3.65 | -4.1 dB  |
| Peaking | 7753 Hz  | 2.6  | -7.0 dB  |
| Peaking | 18873 Hz | 1.2  | -13.6 dB |
| Peaking | 21 Hz    | 0.96 | 3.6 dB   |
| Peaking | 704 Hz   | 1.79 | -2.0 dB  |
| Peaking | 994 Hz   | 1.5  | 2.4 dB   |
| Peaking | 1708 Hz  | 4.4  | -1.3 dB  |
| Peaking | 10842 Hz | 4.05 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.7 dB  |
| Peaking | 62 Hz    | 1.41 | -0.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.0 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -4.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | -1.3 dB |
| Peaking | 8000 Hz  | 1.41 | -4.9 dB |
| Peaking | 16000 Hz | 1.41 | -4.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K712%20PRO/AKG%20K712%20PRO.png)