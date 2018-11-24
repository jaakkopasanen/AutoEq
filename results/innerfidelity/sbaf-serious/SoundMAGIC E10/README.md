# SoundMAGIC E10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.3; 28 -1.8; 31 -2.1; 34 -2.4; 37 -2.7; 41 -3.0; 45 -3.2; 49 -3.5; 54 -3.8; 60 -4.2; 66 -4.5; 72 -4.7; 79 -5.1; 87 -5.5; 96 -5.8; 106 -6.1; 116 -6.3; 128 -6.4; 141 -6.5; 155 -6.5; 170 -6.4; 187 -6.2; 206 -5.9; 227 -5.6; 249 -5.2; 274 -4.8; 302 -4.3; 332 -3.9; 365 -3.4; 402 -2.9; 442 -2.2; 486 -1.5; 535 -1.0; 588 -0.7; 647 -0.3; 712 0.2; 783 0.3; 861 0.3; 947 0.3; 1042 -0.1; 1146 0.2; 1261 1.3; 1387 3.2; 1526 4.1; 1678 4.3; 1846 5.7; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.0; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SoundMAGIC E10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SoundMAGIC E10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.72 | -2.1 dB |
| Peaking | 109 Hz  | 0.88 | -2.9 dB |
| Peaking | 211 Hz  | 0.66 | -4.6 dB |
| Peaking | 2426 Hz | 0.93 | 6.2 dB  |
| Peaking | 5167 Hz | 1.94 | 4.9 dB  |
| Peaking | 1147 Hz | 2.42 | -3.8 dB |
| Peaking | 1288 Hz | 1.06 | 3.0 dB  |
| Peaking | 3912 Hz | 1.62 | 4.3 dB  |
| Peaking | 4323 Hz | 0.65 | -4.1 dB |
| Peaking | 6148 Hz | 4.22 | 3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SoundMAGIC%20E10/SoundMAGIC%20E10.png)