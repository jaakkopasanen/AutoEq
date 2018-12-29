# Bose SoundSport Free
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 21 0.0; 23 2.7; 25 2.3; 28 1.7; 31 1.1; 34 0.7; 37 0.3; 41 -0.2; 45 -0.6; 49 -1.0; 54 -1.3; 60 -1.5; 66 -1.7; 72 -1.8; 79 -1.9; 87 -2.0; 96 -2.1; 106 -2.3; 116 -2.5; 128 -2.5; 141 -2.5; 155 -2.5; 170 -2.4; 187 -2.2; 206 -2.1; 227 -1.8; 249 -1.6; 274 -1.4; 302 -1.2; 332 -1.0; 365 -0.9; 402 -0.8; 442 -0.5; 486 -0.3; 535 -0.2; 588 0.6; 647 0.7; 712 1.2; 783 1.6; 861 1.5; 947 0.6; 1042 -0.3; 1146 -0.7; 1261 -0.9; 1387 -1.2; 1526 -1.9; 1678 -2.7; 1846 -3.4; 2031 -3.6; 2234 -2.8; 2457 -1.6; 2703 -1.0; 2973 -0.9; 3270 -1.2; 3597 -1.5; 3957 -2.0; 4353 -2.7; 4788 -2.3; 5267 -1.6; 5793 -1.5; 6373 -0.2; 7010 1.9; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -1.3; 12418 -3.2; 13660 -3.7; 15026 -4.1; 16529 -1.1; 18182 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.59 | 3.4 dB  |
| Peaking | 120 Hz   | 0.63 | -2.7 dB |
| Peaking | 1941 Hz  | 2.61 | -3.7 dB |
| Peaking | 4426 Hz  | 3.14 | -2.7 dB |
| Peaking | 14216 Hz | 2.23 | -4.6 dB |
| Peaking | 782 Hz   | 1.74 | 3.6 dB  |
| Peaking | 838 Hz   | 0.83 | -1.7 dB |
| Peaking | 6978 Hz  | 9.38 | 2.5 dB  |
| Peaking | 10561 Hz | 2.73 | 1.0 dB  |
| Peaking | 12054 Hz | 5.58 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20Free/Bose%20SoundSport%20Free.png)