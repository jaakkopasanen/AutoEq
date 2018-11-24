# Bose SoundSport Wireless

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.9dB
GraphicEQ: 21 0.0; 23 -0.1; 25 -0.5; 28 -0.8; 31 -1.1; 34 -1.3; 37 -1.5; 41 -1.7; 45 -1.7; 49 -1.7; 54 -1.8; 60 -2.0; 66 -2.1; 72 -2.2; 79 -2.2; 87 -2.3; 96 -2.4; 106 -2.6; 116 -2.7; 128 -2.9; 141 -2.8; 155 -2.8; 170 -2.7; 187 -2.5; 206 -2.3; 227 -2.1; 249 -1.8; 274 -1.6; 302 -1.1; 332 -1.7; 365 -0.7; 402 -0.2; 442 0.1; 486 0.4; 535 0.8; 588 1.2; 647 1.6; 712 1.8; 783 1.7; 861 1.3; 947 0.5; 1042 -0.2; 1146 -0.4; 1261 -0.3; 1387 -0.3; 1526 -0.6; 1678 -1.3; 1846 -2.0; 2031 -2.4; 2234 -1.4; 2457 -0.4; 2703 -0.2; 2973 -0.8; 3270 -2.0; 3597 -3.1; 3957 -4.0; 4353 -5.1; 4788 -4.7; 5267 -2.8; 5793 -0.3; 6373 -0.9; 7010 -2.3; 7711 -0.1; 8482 0.0; 9330 0.0; 10263 0.0; 11289 -0.2; 12418 -0.0; 13660 -2.2; 15026 -2.3; 16529 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose SoundSport Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose SoundSport Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 1.1  | -1.0 dB |
| Peaking | 143 Hz   | 0.57 | -2.8 dB |
| Peaking | 673 Hz   | 1.86 | 2.3 dB  |
| Peaking | 1923 Hz  | 3.85 | -2.3 dB |
| Peaking | 4379 Hz  | 2.56 | -5.3 dB |
| Peaking | 1111 Hz  | 6.04 | -0.7 dB |
| Peaking | 2722 Hz  | 5.08 | 0.9 dB  |
| Peaking | 3385 Hz  | 6.1  | -0.7 dB |
| Peaking | 14301 Hz | 3.81 | -4.3 dB |
| Peaking | 14419 Hz | 1.22 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20SoundSport%20Wireless/Bose%20SoundSport%20Wireless.png)