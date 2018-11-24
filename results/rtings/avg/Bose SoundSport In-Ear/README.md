# Bose SoundSport In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.6; 66 4.3; 72 3.1; 79 2.1; 87 1.1; 96 0.3; 106 -0.4; 116 -0.9; 128 -1.3; 141 -1.6; 155 -1.8; 170 -2.0; 187 -2.1; 206 -2.1; 227 -2.1; 249 -2.1; 274 -2.2; 302 -2.3; 332 -2.3; 365 -2.5; 402 -2.7; 442 -2.7; 486 -2.7; 535 -2.6; 588 -2.3; 647 -1.7; 712 -1.0; 783 -0.3; 861 0.1; 947 0.2; 1042 -0.1; 1146 -0.6; 1261 -1.2; 1387 -2.0; 1526 -2.7; 1678 -3.2; 1846 -3.4; 2031 -3.1; 2234 -1.8; 2457 -0.1; 2703 0.7; 2973 1.1; 3270 1.0; 3597 0.6; 3957 -0.1; 4353 -1.2; 4788 -1.9; 5267 -1.9; 5793 -1.2; 6373 -3.0; 7010 -4.8; 7711 -2.4; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -1.1; 13660 -2.3; 15026 -1.3; 16529 -1.0; 18182 -0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport In-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 0.47 | 9.3 dB  |
| Peaking | 128 Hz   | 0.3  | -4.6 dB |
| Peaking | 1779 Hz  | 3.23 | -3.6 dB |
| Peaking | 6898 Hz  | 4.47 | -4.9 dB |
| Peaking | 13872 Hz | 3.37 | -2.4 dB |
| Peaking | 530 Hz   | 2.69 | -1.1 dB |
| Peaking | 877 Hz   | 3.63 | 1.4 dB  |
| Peaking | 3110 Hz  | 3.34 | 1.8 dB  |
| Peaking | 4820 Hz  | 4.41 | -1.9 dB |
| Peaking | 8810 Hz  | 3.78 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20In-Ear/Bose%20SoundSport%20In-Ear.png)