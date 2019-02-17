# Signature Acoustics Elements C12
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -12.0; 25 -12.4; 28 -13.0; 31 -13.5; 34 -14.0; 37 -14.4; 41 -14.8; 45 -15.2; 49 -15.5; 54 -15.9; 60 -16.4; 66 -16.7; 72 -17.1; 79 -17.5; 87 -17.9; 96 -18.4; 106 -18.5; 116 -18.6; 128 -18.8; 141 -18.9; 155 -18.9; 170 -18.8; 187 -18.6; 206 -18.3; 227 -17.9; 249 -17.5; 274 -17.0; 302 -16.4; 332 -15.7; 365 -15.0; 402 -14.2; 442 -13.2; 486 -12.4; 535 -11.4; 588 -10.1; 647 -8.9; 712 -7.9; 783 -6.6; 861 -5.5; 947 -4.4; 1042 -3.4; 1146 -2.4; 1261 -1.6; 1387 -2.3; 1526 -4.3; 1678 -5.7; 1846 -6.2; 2031 -6.5; 2234 -6.0; 2457 -4.5; 2703 -3.1; 2973 -1.5; 3270 -0.5; 3597 -0.8; 3957 -2.9; 4353 -6.4; 4788 -9.0; 5267 -10.9; 5793 -13.3; 6373 -11.5; 7010 -8.1; 7711 -6.1; 8482 -6.2; 9330 -8.0; 10263 -8.0; 11289 -4.0; 12418 -3.8; 13660 -3.8; 15026 -4.0; 16529 -9.1; 18182 -10.1; 20000 -4.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Signature Acoustics Elements C12 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Signature Acoustics Elements C12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 59 Hz    | 0.3  | -11.0 dB |
| Peaking | 185 Hz   | 0.7  | -7.9 dB  |
| Peaking | 398 Hz   | 1.32 | -5.1 dB  |
| Peaking | 5906 Hz  | 3.05 | -10.0 dB |
| Peaking | 17866 Hz | 1.43 | -7.2 dB  |
| Peaking | 1239 Hz  | 1.84 | 6.5 dB   |
| Peaking | 3149 Hz  | 0.43 | -7.3 dB  |
| Peaking | 3268 Hz  | 1.77 | 10.6 dB  |
| Peaking | 9235 Hz  | 0.76 | 5.5 dB   |
| Peaking | 9686 Hz  | 2.81 | -7.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.6 dB  |
| Peaking | 62 Hz    | 1.41 | -9.4 dB  |
| Peaking | 125 Hz   | 1.41 | -12.1 dB |
| Peaking | 250 Hz   | 1.41 | -11.1 dB |
| Peaking | 500 Hz   | 1.41 | -6.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Signature%20Acoustics%20Elements%20C12/Signature%20Acoustics%20Elements%20C12.png)