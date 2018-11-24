# Bose SoundLink Around-Ear II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -4.0; 31 -4.0; 34 -3.9; 37 -3.7; 41 -3.5; 45 -3.3; 49 -3.1; 54 -2.9; 60 -2.7; 66 -2.6; 72 -2.4; 79 -2.4; 87 -2.3; 96 -2.3; 106 -2.4; 116 -2.5; 128 -2.7; 141 -2.6; 155 -2.5; 170 -2.5; 187 -2.4; 206 -2.3; 227 -2.4; 249 -2.1; 274 -1.8; 302 -1.7; 332 -1.5; 365 -1.2; 402 -1.3; 442 -1.3; 486 -1.0; 535 -0.9; 588 -0.8; 647 -0.8; 712 -0.8; 783 -0.7; 861 -0.3; 947 0.0; 1042 -0.1; 1146 -0.7; 1261 -1.4; 1387 -2.4; 1526 -3.0; 1678 -2.8; 1846 -5.0; 2031 -5.4; 2234 -4.1; 2457 -2.9; 2703 -2.5; 2973 -2.9; 3270 -2.7; 3597 -1.8; 3957 -2.0; 4353 -2.5; 4788 0.2; 5267 5.7; 5793 3.3; 6373 2.3; 7010 2.4; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.5; 16529 -0.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink Around-Ear II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink Around-Ear II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.56 | -3.8 dB |
| Peaking | 173 Hz  | 0.56 | -2.2 dB |
| Peaking | 1999 Hz | 1.89 | -4.9 dB |
| Peaking | 4615 Hz | 2.1  | -7.0 dB |
| Peaking | 5287 Hz | 2.88 | 10.6 dB |
| Peaking | 1000 Hz | 2.81 | 1.9 dB  |
| Peaking | 1051 Hz | 1.24 | -1.0 dB |
| Peaking | 2469 Hz | 3.99 | 0.8 dB  |
| Peaking | 3135 Hz | 3.95 | -1.2 dB |
| Peaking | 3775 Hz | 6.71 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/sbaf-serious/Bose%20SoundLink%20Around-Ear%20II/Bose%20SoundLink%20Around-Ear%20II.png)