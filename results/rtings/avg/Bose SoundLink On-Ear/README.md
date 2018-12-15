# Bose SoundLink On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.3dB
GraphicEQ: 21 -7.2; 23 -7.2; 25 -7.3; 28 -7.3; 31 -7.3; 34 -7.3; 37 -7.2; 41 -7.1; 45 -7.0; 49 -6.8; 54 -6.7; 60 -6.7; 66 -6.7; 72 -6.8; 79 -6.8; 87 -6.8; 96 -6.8; 106 -6.8; 116 -6.7; 128 -6.7; 141 -6.7; 155 -6.7; 170 -6.5; 187 -5.9; 206 -5.5; 227 -5.4; 249 -5.2; 274 -5.3; 302 -5.3; 332 -5.0; 365 -4.6; 402 -4.1; 442 -3.6; 486 -3.1; 535 -2.5; 588 -2.0; 647 -1.5; 712 -1.1; 783 -0.8; 861 -0.6; 947 -0.2; 1042 -0.1; 1146 -0.1; 1261 0.0; 1387 0.0; 1526 -0.1; 1678 -0.6; 1846 -1.1; 2031 -1.8; 2234 -1.8; 2457 -1.2; 2703 -2.2; 2973 -3.0; 3270 -3.1; 3597 -3.7; 3957 -4.6; 4353 -4.1; 4788 -2.7; 5267 -0.7; 5793 0.1; 6373 -1.0; 7010 -3.5; 7711 -5.2; 8482 -6.3; 9330 -6.5; 10263 -5.6; 11289 -4.2; 12418 -3.5; 13660 -3.6; 15026 -5.6; 16529 -10.5; 18182 -13.6; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundLink On-Ear GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-3**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundLink On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.22 | -7.1 dB  |
| Peaking | 152 Hz   | 0.78 | -3.7 dB  |
| Peaking | 346 Hz   | 1.36 | -3.1 dB  |
| Peaking | 7185 Hz  | 0.38 | -3.2 dB  |
| Peaking | 18623 Hz | 1.13 | -14.0 dB |
| Peaking | 1271 Hz  | 1.9  | 1.0 dB   |
| Peaking | 4148 Hz  | 2.07 | -2.8 dB  |
| Peaking | 5801 Hz  | 2.11 | 6.4 dB   |
| Peaking | 8581 Hz  | 1.06 | -4.0 dB  |
| Peaking | 12778 Hz | 2.03 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundLink%20On-Ear/Bose%20SoundLink%20On-Ear.png)