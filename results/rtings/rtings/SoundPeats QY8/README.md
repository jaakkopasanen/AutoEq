# SoundPeats QY8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 21 -6.2; 23 -6.1; 25 -6.0; 28 -5.8; 31 -5.6; 34 -5.3; 37 -5.1; 41 -4.8; 45 -4.4; 49 -4.2; 54 -4.0; 60 -4.0; 66 -3.9; 72 -3.9; 79 -3.9; 87 -3.9; 96 -4.0; 106 -4.1; 116 -4.3; 128 -4.8; 141 -5.6; 155 -5.9; 170 -5.7; 187 -5.2; 206 -4.7; 227 -4.3; 249 -3.8; 274 -3.3; 302 -2.8; 332 -2.3; 365 -1.8; 402 -1.3; 442 -0.8; 486 -0.3; 535 0.3; 588 0.9; 647 1.5; 712 1.7; 783 1.7; 861 1.3; 947 0.5; 1042 -0.4; 1146 -1.4; 1261 -2.0; 1387 -2.4; 1526 -2.9; 1678 -3.7; 1846 -5.2; 2031 -7.0; 2234 -7.2; 2457 -6.8; 2703 -6.0; 2973 -4.8; 3270 -4.4; 3597 -5.0; 3957 -6.8; 4353 -9.6; 4788 -8.8; 5267 -3.9; 5793 -0.4; 6373 -0.7; 7010 -2.1; 7711 -4.4; 8482 -4.5; 9330 -4.9; 10263 -6.2; 11289 -4.0; 12418 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundPeats QY8 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundPeats QY8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.21 | -6.2 dB |
| Peaking | 172 Hz   | 1.12 | -5.1 dB |
| Peaking | 2260 Hz  | 1.79 | -7.3 dB |
| Peaking | 4440 Hz  | 3.97 | -9.4 dB |
| Peaking | 9769 Hz  | 2.44 | -6.1 dB |
| Peaking | 312 Hz   | 2.42 | -0.8 dB |
| Peaking | 717 Hz   | 2.31 | 2.7 dB  |
| Peaking | 6020 Hz  | 4.01 | 4.9 dB  |
| Peaking | 6355 Hz  | 1.42 | -2.4 dB |
| Peaking | 12929 Hz | 3.6  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/rtings/SoundPeats%20QY8/SoundPeats%20QY8.png)