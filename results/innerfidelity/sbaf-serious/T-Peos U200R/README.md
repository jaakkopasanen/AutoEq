# T-Peos U200R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.9; 23 -11.9; 25 -11.9; 28 -11.9; 31 -11.9; 34 -11.9; 37 -11.9; 41 -11.9; 45 -11.9; 49 -11.9; 54 -12.0; 60 -12.1; 66 -12.2; 72 -12.3; 79 -12.5; 87 -12.7; 96 -12.9; 106 -13.0; 116 -12.9; 128 -13.0; 141 -13.1; 155 -13.0; 170 -12.9; 187 -12.7; 206 -12.5; 227 -12.1; 249 -11.8; 274 -11.4; 302 -11.0; 332 -10.5; 365 -10.0; 402 -9.5; 442 -8.9; 486 -8.5; 535 -8.0; 588 -7.2; 647 -6.7; 712 -6.5; 783 -6.0; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.2; 1387 -7.9; 1526 -8.7; 1678 -9.2; 1846 -9.2; 2031 -8.8; 2234 -7.8; 2457 -5.4; 2703 -3.5; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -1.5; 4353 -6.2; 4788 -11.4; 5267 -9.4; 5793 -3.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -7.0; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`T-Peos U200R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos U200R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 34 Hz    | 0.2  | -5.3 dB  |
| Peaking | 189 Hz   | 0.74 | -3.9 dB  |
| Peaking | 3577 Hz  | 1.84 | 13.6 dB  |
| Peaking | 5123 Hz  | 1.19 | -24.2 dB |
| Peaking | 5926 Hz  | 1.51 | 20.5 dB  |
| Peaking | 869 Hz   | 1.78 | 1.8 dB   |
| Peaking | 1904 Hz  | 1.73 | -2.4 dB  |
| Peaking | 2735 Hz  | 4.23 | 2.4 dB   |
| Peaking | 9501 Hz  | 5.61 | -1.9 dB  |
| Peaking | 12213 Hz | 1.19 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20U200R/T-Peos%20U200R.png)