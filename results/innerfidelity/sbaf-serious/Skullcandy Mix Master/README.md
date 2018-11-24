# Skullcandy Mix Master

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.3; 25 3.6; 28 2.7; 31 2.0; 34 1.6; 37 1.2; 41 0.9; 45 0.7; 49 0.5; 54 0.3; 60 0.2; 66 0.2; 72 0.1; 79 -0.3; 87 -0.7; 96 -1.2; 106 -1.3; 116 -1.5; 128 -1.8; 141 -2.1; 155 -2.3; 170 -2.2; 187 -2.5; 206 -2.7; 227 -2.6; 249 -2.3; 274 -1.8; 302 -1.5; 332 -1.5; 365 -1.0; 402 -1.1; 442 -0.6; 486 -0.2; 535 0.7; 588 1.5; 647 1.6; 712 1.4; 783 1.4; 861 0.6; 947 0.0; 1042 -0.0; 1146 -0.2; 1261 -0.9; 1387 -2.2; 1526 -2.8; 1678 -3.0; 1846 -2.0; 2031 -1.4; 2234 -0.0; 2457 1.9; 2703 3.5; 2973 4.8; 3270 5.5; 3597 2.0; 3957 -1.4; 4353 0.8; 4788 3.2; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Skullcandy Mix Master GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Mix Master ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.25 | 5.5 dB  |
| Peaking | 184 Hz  | 1.07 | -2.8 dB |
| Peaking | 1649 Hz | 3.13 | -3.6 dB |
| Peaking | 3018 Hz | 4.09 | 5.7 dB  |
| Peaking | 5762 Hz | 3.4  | 6.8 dB  |
| Peaking | 641 Hz  | 0.66 | -1.8 dB |
| Peaking | 671 Hz  | 1.47 | 3.7 dB  |
| Peaking | 3963 Hz | 1.9  | 2.5 dB  |
| Peaking | 3991 Hz | 5.65 | -5.8 dB |
| Peaking | 8276 Hz | 3.86 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Mix%20Master/Skullcandy%20Mix%20Master.png)