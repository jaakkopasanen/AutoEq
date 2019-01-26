# Focal Elear
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.8; 37 5.4; 41 4.7; 45 4.1; 49 3.6; 54 3.1; 60 2.5; 66 1.9; 72 1.3; 79 0.9; 87 0.4; 96 0.1; 106 -0.3; 116 -0.7; 128 -1.0; 141 -1.3; 155 -1.5; 170 -1.5; 187 -1.3; 206 -1.1; 227 -0.9; 249 -0.7; 274 -0.6; 302 -0.6; 332 -0.5; 365 -0.3; 402 -0.3; 442 -0.4; 486 -0.4; 535 -0.2; 588 -0.1; 647 -0.0; 712 0.1; 783 0.2; 861 0.2; 947 0.1; 1042 -0.0; 1146 -0.1; 1261 -0.5; 1387 -1.0; 1526 -1.2; 1678 -1.3; 1846 -1.3; 2031 -1.3; 2234 0.1; 2457 0.0; 2703 -0.1; 2973 -0.6; 3270 -0.2; 3597 1.6; 3957 5.4; 4353 6.0; 4788 6.0; 5267 6.0; 5793 3.9; 6373 2.9; 7010 2.5; 7711 0.3; 8482 -2.8; 9330 -1.9; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -3.5; 18182 -8.5; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Focal Elear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Focal Elear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.62 | 6.3 dB   |
| Peaking | 146 Hz   | 0.94 | -2.0 dB  |
| Peaking | 4113 Hz  | 0.59 | -4.2 dB  |
| Peaking | 4732 Hz  | 1.47 | 10.9 dB  |
| Peaking | 19533 Hz | 1.05 | -12.9 dB |
| Peaking | 3250 Hz  | 8.31 | -1.3 dB  |
| Peaking | 8696 Hz  | 4.98 | -5.9 dB  |
| Peaking | 8751 Hz  | 1.43 | 2.0 dB   |
| Peaking | 15041 Hz | 1.74 | 2.2 dB   |
| Peaking | 17336 Hz | 2.12 | -2.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Focal%20Elear/Focal%20Elear.png)