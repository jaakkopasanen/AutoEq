# Bose SoundSport Free

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 0.0; 23 3.1; 25 2.5; 28 1.8; 31 1.2; 34 0.6; 37 0.2; 41 -0.4; 45 -0.9; 49 -1.3; 54 -1.6; 60 -1.8; 66 -1.9; 72 -1.8; 79 -1.7; 87 -1.6; 96 -1.7; 106 -1.8; 116 -2.0; 128 -2.0; 141 -2.0; 155 -1.9; 170 -1.7; 187 -1.6; 206 -1.6; 227 -1.4; 249 -1.0; 274 -0.7; 302 -0.3; 332 -0.1; 365 0.1; 402 0.3; 442 0.6; 486 0.9; 535 1.0; 588 1.7; 647 1.8; 712 2.0; 783 2.1; 861 1.7; 947 0.7; 1042 -0.3; 1146 -0.5; 1261 -0.7; 1387 -1.2; 1526 -2.2; 1678 -3.0; 1846 -3.3; 2031 -3.2; 2234 -2.4; 2457 -1.2; 2703 -0.2; 2973 0.6; 3270 1.4; 3597 1.6; 3957 0.4; 4353 -1.4; 4788 -0.7; 5267 1.4; 5793 2.4; 6373 3.6; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Free GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-42**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Free ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.95 | 4.8 dB  |
| Peaking | 77 Hz   | 0.32 | -2.3 dB |
| Peaking | 669 Hz  | 1.37 | 2.5 dB  |
| Peaking | 1800 Hz | 2.31 | -3.8 dB |
| Peaking | 6421 Hz | 4.48 | 4.1 dB  |
| Peaking | 856 Hz  | 4.07 | 1.5 dB  |
| Peaking | 960 Hz  | 2.17 | -1.1 dB |
| Peaking | 3530 Hz | 3.24 | 2.2 dB  |
| Peaking | 4232 Hz | 6.59 | -1.4 dB |
| Peaking | 4561 Hz | 9.24 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundSport%20Free/Bose%20SoundSport%20Free.png)