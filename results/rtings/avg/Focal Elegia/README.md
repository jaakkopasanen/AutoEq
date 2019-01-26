# Focal Elegia
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 1.6; 25 1.5; 28 1.5; 31 1.5; 34 1.7; 37 2.0; 41 2.2; 45 2.2; 49 2.1; 54 2.0; 60 1.9; 66 1.8; 72 1.6; 79 1.4; 87 1.2; 96 1.2; 106 1.1; 116 1.2; 128 1.5; 141 1.7; 155 1.7; 170 1.7; 187 1.4; 206 1.0; 227 0.4; 249 -0.1; 274 -0.6; 302 -1.0; 332 -1.2; 365 -1.2; 402 -1.2; 442 -1.4; 486 -1.4; 535 -1.1; 588 -0.8; 647 -0.5; 712 -0.3; 783 -0.1; 861 -0.1; 947 -0.1; 1042 0.2; 1146 0.6; 1261 0.2; 1387 -0.5; 1526 -1.0; 1678 -1.6; 1846 -1.5; 2031 1.1; 2234 2.5; 2457 1.9; 2703 2.0; 2973 2.2; 3270 5.9; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.9; 5793 2.3; 6373 2.8; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -1.3; 18182 -6.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elegia GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elegia ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 0.71 | 2.2 dB  |
| Peaking | 154 Hz   | 2.97 | 1.6 dB  |
| Peaking | 3505 Hz  | 3.19 | 4.4 dB  |
| Peaking | 4825 Hz  | 2.06 | 5.5 dB  |
| Peaking | 19008 Hz | 1.27 | -7.6 dB |
| Peaking | 419 Hz   | 1.62 | -1.6 dB |
| Peaking | 1796 Hz  | 3.68 | -3.0 dB |
| Peaking | 2158 Hz  | 4.51 | 2.7 dB  |
| Peaking | 16107 Hz | 2.19 | 2.0 dB  |
| Peaking | 18424 Hz | 2.48 | -1.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elegia/Focal%20Elegia.png)