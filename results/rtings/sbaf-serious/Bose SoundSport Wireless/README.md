# Bose SoundSport Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 21 0.0; 23 0.2; 25 -0.2; 28 -0.7; 31 -1.0; 34 -1.4; 37 -1.6; 41 -1.9; 45 -2.0; 49 -2.1; 54 -2.2; 60 -2.2; 66 -2.3; 72 -2.2; 79 -2.0; 87 -1.9; 96 -2.0; 106 -2.2; 116 -2.2; 128 -2.3; 141 -2.3; 155 -2.2; 170 -2.1; 187 -1.9; 206 -1.8; 227 -1.6; 249 -1.3; 274 -0.9; 302 -0.3; 332 -0.8; 365 0.3; 402 0.9; 442 1.2; 486 1.6; 535 2.0; 588 2.3; 647 2.6; 712 2.7; 783 2.2; 861 1.4; 947 0.5; 1042 -0.2; 1146 -0.2; 1261 -0.1; 1387 -0.3; 1526 -1.0; 1678 -1.6; 1846 -2.0; 2031 -2.0; 2234 -0.9; 2457 0.1; 2703 0.6; 2973 0.7; 3270 0.6; 3597 0.1; 3957 -1.6; 4353 -3.8; 4788 -3.1; 5267 0.2; 5793 3.6; 6373 2.9; 7010 0.8; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 104 Hz  | 0.35 | -2.4 dB |
| Peaking | 604 Hz  | 1.36 | 3.2 dB  |
| Peaking | 1810 Hz | 3.22 | -2.3 dB |
| Peaking | 4552 Hz | 5.28 | -5.0 dB |
| Peaking | 5980 Hz | 4.6  | 4.5 dB  |
| Peaking | 16 Hz   | 0.32 | 1.8 dB  |
| Peaking | 39 Hz   | 1.02 | -1.6 dB |
| Peaking | 750 Hz  | 6.21 | 0.8 dB  |
| Peaking | 1967 Hz | 0.36 | -0.4 dB |
| Peaking | 2927 Hz | 2.69 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundSport%20Wireless/Bose%20SoundSport%20Wireless.png)